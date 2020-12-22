from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.urls import path
from agroplace.apps.system.views import home
from agroplace.apps.users.views import register, login
from agroplace.apps.orders.views import cart
from agroplace.apps.products.views import product

admin.autodiscover()
admin.site.site_header = 'AGROPLACE - ADMINISTRATION'
admin.site.site_title = 'AGROPLACE - ADMINISTRATION'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^product/(?P<pk>\d+)/$', product, name='product'),
    url(r'^$', home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
