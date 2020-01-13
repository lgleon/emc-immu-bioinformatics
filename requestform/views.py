from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Jobs, AnalysisType, GeneralQuestions
from .request import RequestJobs, GeneralInfo, AnalysisType

def index(request):
    return HttpResponse("Hello, world. I am in the request form ")

#def testing(request):
#    current_user = "Mable Marbles"
#    return render (request, 'test.html',
#                   {'date': datetime.now(), 'login': current_user})


def job_request(request):
    submitted = False
    if request.method == 'POST':
        form = RequestJobs(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/job_request/?submitted=True')
    else:
        form = RequestJobs()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'job_request.html', {'form': form, 'submitted' : submitted})


def general_info(request):
    submitted = False
    if request.method == 'POST':
        form = GeneralInfo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/general_info/?submitted=True')
    else:
        form = GeneralInfo()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'general_info.html', {'form': form, 'submitted': submitted})


def analysis_type(request):
    submitted = False
    if request.method == 'POST':
        form = AnalysisType(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/analysis_type/?submitted=True')
    else:
        form = AnalysisType()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'analysis_type.html', {'form': form, 'submitted': submitted})
