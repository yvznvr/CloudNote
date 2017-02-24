from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class NoteBook(models.Model):
    title = models.CharField(verbose_name='Başlık', max_length=250)
    info = models.TextField(verbose_name='İçerik')
    linked_user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-update', kwargs={'pk':self.id})

    class Meta:
        verbose_name = 'Notlar'
        verbose_name_plural = 'Notlar'





