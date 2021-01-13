from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Categories
from agroplace.apps.orders.models import Cart


def product(request, pk):

    product = get_object_or_404(Products, id=pk)
    related = Products.objects.filter(status=1).exclude(id=product.id).order_by('?')
    page_title = product.name
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('/login/?next=/product/{}/'.format(product.id))
        if Products.objects.filter(id=request.POST['product_id']).exists():
            existed, new = Cart.objects.get_or_create(product_id=request.POST['product_id'], user=request.user)
            if existed:
                existed.qty += int(request.POST['quantity'])
                existed.save()
            elif new:
                new.qty = int(request.POST['quantity'])
                new.save()
            product_added_tocart = True


    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'pages/product.html', locals())


def category(request, pk):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()

    main_cats = Categories.objects.filter(status=True)
    category = get_object_or_404(Categories, id=pk)
    products = Products.objects.filter(status=1, category=category)
    page_title = category.name
    return render(request, 'pages/category.html', locals())
