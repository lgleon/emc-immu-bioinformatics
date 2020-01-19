from django import forms
from django.forms import ModelForm
from .models import Clients



class Clients_data(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Clients
        fields = '__all__'
