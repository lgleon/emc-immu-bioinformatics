from django import forms
from django.forms import ModelForm
from .models import Jobs



class RequestJobs(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Jobs
        fields = '__all__'
