from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from agroplace.apps.orders.models import Orders, Cart, ProductsInOrders


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['comment', 'country', 'region', 'postal_code']

    def clean(self):
        form_data = self.cleaned_data
        if not get_cart_count(self.user):
            raise forms.ValidationError("Products are not found")
            # self._errors[None] = ["Password do not match"]  # Will raise a error message
        return form_data


def get_cart_count(user) -> int:
    cart_count = 0
    if user.is_authenticated:
        cart_count = Cart.objects.filter(user=user).count()
    return cart_count


@login_required(login_url='/login')
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    if request.method == "POST":
        form = OrdersForm(request.POST)
        form.user = request.user

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            new_order = post.save()
            for c in cart:
                ProductsInOrders.objects.create(
                    order=post,
                    product=c.product,
                    cost=c.product.cost,
                    name=c.product.name,
                    qty=c.qty
                )
            cart.delete()
            return redirect('/orders')
    else:
        order_form = OrdersForm()

    # cart = Cart.objects.filter(user=request.user)
    if request.GET.get('delete'):
        Cart.objects.filter(product_id=request.GET['delete'], user=request.user).delete()

    cart_count = get_cart_count(request.user)
    page_title = _('Cart')
    return render(request, 'pages/cart.html', locals())


@login_required(login_url='/login')
def orders(request):
    user_orders = Orders.objects.filter(user=request.user).order_by('-id')
    cart_count = get_cart_count(request.user)
    page_title = _('My orders')
    return render(request, 'pages/orders.html', locals())
