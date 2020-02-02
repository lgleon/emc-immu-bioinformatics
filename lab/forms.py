from django import forms
from django.forms import ModelForm
from .models import Team
from django.utils import timezone, dateformat

class JobStatus(forms.Form):
    """
        Create the form to make job status update for the team members
    """
    name = forms.CharField(max_length=10, label='Team member', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Team member'}),)
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    job_name = forms.CharField(max_length=30, label='Job name, id', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job name'}))
    #date = forms.DateTimeField(widget=forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Date'}))
    jobstatus_update = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update job status'}))
