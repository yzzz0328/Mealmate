from django import forms
from django.forms import ModelForm
from .models import Entry

# Creating a form function that is connected to the Entry model database so submissions would be added into the database.
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            'author',
            'happiness',
            'energy',
            'hunger',
            'calmness',
            'health',
            'journal',
        ]

