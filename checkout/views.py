from django.shortcuts import render
from django.http import HttpResponse
import stripe
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from requestform.models import Jobs
from requestform.views import job_submited

stripe.api_key = settings.STRIPE_SECRET

""" 
aqui he cambiado Product por Priority que es lo que la gente esta comprando en el mi app, 
quantity is refer to priority-level, more quantity more level 
"""

def index(request):
    return HttpResponse("Hello, world. I am in the checkout")




@login_required(login_url='/users/login')
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        jobs = Jobs.objects.filter(is_payed=False, usuario=request.user)
        print("is the form valid¿")
        if order_form.is_valid() and payment_form.is_valid():
            print("it is!")
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()
            print(type(order))
            total = 0
            for job in jobs:
                total += 20 + job.get_priority_value()
                order_line_item = OrderLineItem(
                    order=order,
                    job=job,
                )
                order_line_item.save()

            try:
                print("before charge create")
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                print("card problem")
                messages.error(request, "Your card was declined!")

            if customer.paid:
                print("wont see this")
                messages.error(request, "You have successfully paid")
                for job in jobs:
                    job.is_payed = True
                    job.save()
                return redirect(reverse('job_submited')) ## change to job paid
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        current_user = request.user
        jobs = Jobs.objects.filter(is_payed=False, usuario=current_user)
        for job in jobs:
            print(job.job_name)
            print(job.priority_status)

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'jobs':jobs, 'publishable': settings.STRIPE_PUBLISHABLE})


