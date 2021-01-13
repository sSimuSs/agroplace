from django.shortcuts import render
from agroplace.apps.banners.models import MainBanners
from agroplace.apps.products.models import Products, Categories
from agroplace.apps.orders.models import Cart

def home(request):
    main_banners = MainBanners.objects.filter(status=True)
    products = Products.objects.filter(status=True).order_by('-id')
    categories = Categories.objects.filter(status=True)
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'pages/home.html', locals())
