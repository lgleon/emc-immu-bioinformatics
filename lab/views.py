from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Team
from .forms import JobStatus
from django.shortcuts import get_object_or_404


#def index(request):
#return HttpResponse("Hello, world. I am in the lab lost with Alice in wonderland")


def index(request):
    return render(request, 'index.html')

def work(request):
    return render(request, 'work.html')

def team(request):
    return render(request, 'team.html')

@login_required(login_url='/users/login')
def job_status(request):
    submitted = False
    if request.user.is_staff:

        if request.method == 'POST':
            form = JobStatus(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                # assert False
                return HttpResponseRedirect('/job_status/?submitted=True')
        else:
            form = JobStatus()
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'job_status.html', {'form': form, 'submitted' : submitted})

    else:
        return render(request, 'index.html')





"""  
In the template:
{% if user.is_staff %}
    <p>Hello, Team.</p>
{% else %}
    <p>Hello, ordinary visitor.</p>
{% endif %}



In the view:
if request.user.is_superuser:
    # Hello, admin.
else:
    # Hello, ordinary visitor.

"""