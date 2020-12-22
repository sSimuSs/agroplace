from django.shortcuts import render, get_object_or_404
from .models import Products


def product(request, pk):
    product = get_object_or_404(Products, id=pk)
    return render(request, 'pages/product.html', {'product': product})
