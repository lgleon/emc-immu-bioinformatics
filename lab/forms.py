from django import forms
from django.forms import ModelForm
from .models import JobStatus

class JobStatus(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = JobStatus
        fields = '__all__'
