from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from requestform.models import Jobs

# Create your views here.

def view_cart(request):
    """A View that renders the cart contents"""
    cart = Jobs.objects.all()
    print(cart)
    return render(request, "cart.html",
                  {'cart': cart})



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
