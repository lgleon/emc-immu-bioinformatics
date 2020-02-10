from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Jobs
from .request import RequestJobs
import logging
from django.template import RequestContext
from django.template import loader

logger = logging.getLogger(__name__)
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '/tmp/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})


def index(request):
    logger.error("Call me baby!")
    logger.warning("Call me baby!")
    logger.info("Call me baby!")
    return HttpResponse('<iframe width="560" height="315" src="https://www.youtube.com/embed/fQGbXmkSArs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


def job_submited(request):
    jobs = Jobs.objects.filter(is_payed=False, usuario=request.user)
    return render(request, 'job_request_submited.html', {'jobs': jobs})


@login_required(login_url='/users/login')
def job_request(request):
    logger.error("This is an error")
    logger.warning("This is a warning")
    logger.info("This is just info about what´s going on")
    submitted = False
    user = request.user
    if request.method == 'POST':
        form = RequestJobs(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.usuario = request.user
            job.save()
            return HttpResponseRedirect('/requestform/job_submited', {'user': user})

    else:
        form = RequestJobs()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'job_request.html', {'form': form, 'submitted': submitted})

