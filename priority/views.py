from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Clients_data
from .models import Clients
from django.template import RequestContext

def index(request):
    return HttpResponse("Hello, world. I am in the priority part")

def client_submited(request):
    clients = Clients.objects.filter(user=request.user)
    return render(request, 'client_submited.html', {'clients': clients})

@login_required(login_url='/users/login')
def clients_data(request):
    submitted = False
    user = request.user
    if request.method == 'POST':
        form = Clients_data(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return HttpResponseRedirect('/priority/client_submited', {'user':user})
    else:
        form = Clients_data()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'clients.html', {'form': form, 'submitted': submitted})

