from django import forms
from django.forms import ModelForm
from .models import Clients



class Clients_data(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Clients
        fields = ['department', 'supervisor', 'project']
        widgets = {
            #'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'user name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'supervisor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor'}),
            'project': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
        }
