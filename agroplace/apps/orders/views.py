from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from agroplace.apps.orders.models import Orders, Cart


@login_required(login_url='/login')
def cart(request):

    cart = Cart.objects.filter(user=request.user)
    if request.GET.get('delete'):
        Cart.objects.filter(product_id=request.GET['delete'], user=request.user).delete()

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'pages/cart.html', locals())
