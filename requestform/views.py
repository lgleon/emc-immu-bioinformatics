from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. I am in the request form ")

def testing(request):
    current_user = "Mable Marbles"
    return render (request, 'test.html',
                   {'date': datetime.now(), 'login': current_user})