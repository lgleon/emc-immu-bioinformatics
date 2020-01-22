from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .forms import Contact

# Create your views here.


def index(request):
    return HttpResponse("Hello, Hello, We are in teh contact index")



def contact(request):
    submitted = False
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact/?submitted=True')
    else:
        form = Contact()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact/contact.html', {'form': form, 'submitted' : submitted})
