from django import forms
from django.forms import ModelForm
from .models import Jobs, GeneralQuestions, AnalysisType



class RequestJobs(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Jobs
        fields = '__all__'


class GeneralInfo(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = GeneralQuestions
        fields = '__all__'


class AnalysisType(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = AnalysisType
        fields = '__all__'
