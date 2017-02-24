from django import forms
from django.contrib.auth.models import User
from .models import NoteBook


class UserForm(forms.Form):
    user_name = forms.CharField(label='Kullanıcı adı')
    password = forms.CharField(widget=forms.PasswordInput(), label='Parola')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['info'].widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = NoteBook
        fields = ['title', 'info']

class CreateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = forms.CharField(widget=forms.PasswordInput(), label='Parola')
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})


    class Meta:
        model = User
        fields = ['username', 'password']



