from django.shortcuts import render, get_object_or_404
from .models import Products, Categories


def product(request, pk):
    product = get_object_or_404(Products, id=pk)
    related = Products.objects.filter(status=1).exclude(id=product.id).order_by('?')
    page_title = product.name
    return render(request, 'pages/product.html', locals())


def category(request, pk):
    main_cats = Categories.objects.filter(status=True)
    category = get_object_or_404(Categories, id=pk)
    products = Products.objects.filter(status=1, category=category)
    page_title = category.name
    return render(request, 'pages/category.html', locals())
