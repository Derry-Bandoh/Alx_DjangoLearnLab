from django import forms
from django.core.validators import validate_slug, RegexValidator
from .models import Book

class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9\s\-\.\,]*$',
                'Only letters, numbers, spaces, and basic punctuation are allowed.'
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Search books...',
            'class': 'form-control'
        })
    )