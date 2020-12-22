from django.shortcuts import render
from agroplace.apps.banners.models import MainBanners


def home(request):
    main_banners = MainBanners.objects.filter(status=True)
    return render(request, 'pages/home.html', {'banners':main_banners})