from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from requestform.models import Jobs
from checkout.forms import MakePaymentForm, OrderForm
from checkout.models import OrderLineItem
# Create your views here.

@login_required(login_url='/users/login')
def view_cart(request):
    """A View that renders the cart contents"""
    current_user = request.user
    cart = Jobs.objects.filter(is_payed=False, usuario=current_user)
    total = 0
    for item in cart:
        total += 20 + item.get_priority_value()
    #print(my_cart)

    #Jobs.PRIORITY_CHOICES, look for options to put this selection onto html directly
    return render(request, "cart.html", {'cart': cart, 'total': total})


@login_required(login_url='/users/login')
def adjust_cart(request, id):
    current_user = request.user
    cart = Jobs.objects.filter(is_payed=False, usuario=current_user)
    prioirty = Jobs.objects.update( usuario=current_user)

    return redirect(reverse('view_cart', {'cart':cart, 'priority':prioirty}))
