from django import forms
from django.forms import ModelForm
from .models import Clients



class Clients_data(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Clients
        fields = '__all__'
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Who is requesting this job'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'supervisor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor'}),
            'project': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
        }
