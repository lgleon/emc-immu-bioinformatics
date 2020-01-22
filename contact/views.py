from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Contact


# Create your views here.


def index(request):
    return HttpResponse("Hello, Hello, We are in teh contact index")


def contact(request):
    if request.method == 'GET':
        form = Contact()
    else:
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')



"""
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

"""