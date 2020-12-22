from django.shortcuts import render
from agroplace.apps.banners.models import MainBanners
from agroplace.apps.products.models import Products


def home(request):
    main_banners = MainBanners.objects.filter(status=True)
    products = Products.objects.filter(status=True).order_by('-id')
    content = {'banners': main_banners, 'products': products}
    return render(request, 'pages/home.html', content)
