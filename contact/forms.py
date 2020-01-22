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