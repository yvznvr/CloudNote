from rest_framework import serializers
from .models import NoteBook


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = ['id', 'title', 'info']