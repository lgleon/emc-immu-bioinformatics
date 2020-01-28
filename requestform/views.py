from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Jobs
from .request import RequestJobs
import logging

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

#def testing(request):
#    current_user = "Mable Marbles"
#    return render (request, 'test.html',
#                   {'date': datetime.now(), 'login': current_user})

def job_submited():
    return render(request, 'job_request_submited.html')

@login_required(login_url='/users/login')
def job_request(request):
    logger.error("This is an error")
    logger.warning("This is a warning")
    logger.info("This is just info about what´s going on")
    submitted = False
    if request.method == 'POST':
        form = RequestJobs(request.POST)
        if form.is_valid():
            form.save()
            logger.info("The job id %s", form.auto_id)
            return HttpResponseRedirect('/requestform/job_submited')

    else:
        form = RequestJobs()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'job_request.html', {'form': form, 'submitted' : submitted})

