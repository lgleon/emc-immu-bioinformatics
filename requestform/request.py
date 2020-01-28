from django import forms
from django.forms import ModelForm
from .models import Jobs



class RequestJobs(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Jobs
        fields = '__all__'
        widgets = {
            'job_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job name'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user, supervisor'}),
            'priority_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Priority status'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'research_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Research question'}),
            'sample_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sample number'}),
            'expectations': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'what do you expect'}),
            'deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dead line'}),
            'data_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type of data: DNA, RNA etc'}),
            'alignment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'aligment'}),
            'annotation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'annotation'}),
            'de_analysis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Differential Expresion'}),
            'other_analysis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other type of analysis'}),
            'detailed_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Detailed research question'}),
            'detailed_summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Detailed summary'}),
            'other_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other info'}),
            'subm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other info'}),



        }
