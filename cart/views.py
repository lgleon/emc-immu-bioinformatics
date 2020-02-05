from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from requestform.models import Jobs
from checkout.forms import MakePaymentForm, OrderForm
from checkout.models import OrderLineItem
# Create your views here.

def view_cart(request):
    """A View that renders the cart contents"""
    current_user = request.user
    cart = Jobs.objects.filter(is_payed=False, usuario=current_user)
    total = 0
    for item in cart:
        total += 20 + item.get_priority_value()
    #print(my_cart)
    return render(request, "cart.html", {'cart': cart, 'total': total})



def adjust_cart(request, id):
    """
    Adjust the quantity is related with level of priority (0==none, 1==Low, 2==Mid and
    3==High), in case user made a mistake when it was submitted
    """
    print(request.POST)
    priority = request.POST.get('priority_status')
    cart = request.session.get('cart', {})

    if priority > 0:
        cart[id] = priority
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
