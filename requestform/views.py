from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Jobs
from .request import RequestJobs

def index(request):
    return HttpResponse("Hello, world. I am in the request form ")

#def testing(request):
#    current_user = "Mable Marbles"
#    return render (request, 'test.html',
#                   {'date': datetime.now(), 'login': current_user})

@login_required(login_url='/users/login')
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

