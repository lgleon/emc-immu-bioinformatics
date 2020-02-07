from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Contact

# Create your views here.
def index(request):
    return HttpResponse("Hello, Hello, We are in the contact index")


def success(request):
    return render(request, 'contact/contact_done.html')

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            print("valid contact form")
            form.save()
            return HttpResponseRedirect('/contact/success')

    else:
        form = Contact()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html', {'contact_form': form, 'submitted': submitted})

