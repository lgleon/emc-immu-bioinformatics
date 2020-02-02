from django import forms
from django.contrib.auth.models import User


class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password1'}),
        'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password2'}),
    }