from django.shortcuts import render, get_object_or_404
from .models import Products


def product(request, pk):
    product = get_object_or_404(Products, id=pk)
    related = Products.objects.filter(status=1).exclude(id=product.id)
    page_title = product.name
    return render(request, 'pages/product.html', locals())
