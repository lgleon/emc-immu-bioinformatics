from django import forms
from django.forms import ModelForm
from .models import Jobs


class RequestJobs(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Jobs
        fields= [
            'job_name','priority_status','subject','research_question','sample_number','expectations','deadline',
            'data_type', 'alignment','annotation','de_analysis', 'other_analysis','detailed_question',
            'detailed_summary', 'other_info'
        ]
        widgets = {
            'job_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job name'}),
            #'usuario': forms.Select(attrs={'class': 'form-control', 'placeholder': 'user, supervisor'}),
            'priority_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Priority status'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'research_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Research question'}),
            'sample_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'sample number'}),
            'expectations': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'what do you expect'}),
            'deadline': forms.SelectDateWidget(attrs={'type': 'date', 'class': 'form-control'}),
            'data_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type of data: DNA, RNA etc'}),
            'alignment': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'annotation': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'de_analysis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Differential Expresion'}),
            'other_analysis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other type of analysis'}),
            'detailed_question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detailed research question'}),
            'detailed_summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detailed summary'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Other info'}),
        }
