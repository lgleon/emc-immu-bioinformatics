from django import forms
from django.forms import ModelForm
from .models import Contact
from django.utils import timezone, dateformat

class Contact(ModelForm):
    """
            Create the form for contact
    """
    required_css_class = 'required'
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact email'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institution'}),
            'inquiry': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Question'})
        }