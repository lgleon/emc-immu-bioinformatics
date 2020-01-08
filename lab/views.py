from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Team
from .models import JobStatus



def index(request):
    return HttpResponse("Hello, world. I am in the lab lost with Alice in wonderland")

#def testing(request):
#    current_user = "Mable Marbles"
#    return render(request, 'test.html', {'date': datetime.now(), 'login': current_user})


def job_status(request):
    submitted = False
    if request.method == 'POST':
        form = JobStatus(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/job_status/?submitted=True')
    else:
        form = JobStatus()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'job_status.html', {'form': form, 'submitted' : submitted})
