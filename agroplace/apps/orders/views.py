from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from agroplace.apps.orders.models import Orders, Cart


@login_required(login_url='/login')
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'pages/cart.html', {'cart': cart})
