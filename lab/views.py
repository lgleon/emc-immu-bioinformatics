from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Team
from .models import JobStatus


#def index(request):
#∫    return HttpResponse("Hello, world. I am in the lab lost with Alice in wonderland")

def testing(request):
    current_user = "Mable Marbles"
    return render(request, 'test.html', {'date': datetime.now(), 'login': current_user})