from django import forms
from django.forms import ModelForm
from .models import Team
from django.utils import timezone, dateformat

class JobStatus(forms.Form):
    """
        Create the form to make job status update for the team members
        """
    name = forms.CharField(max_length=5, label='Name of the team member working in this job')
    email = forms.EmailField(required=True)
    job_name = forms.CharField(max_length=30, label='Name of the Job to update')
    date = forms.DateTimeField()
    jobstatus_update = forms.CharField(max_length=300)
