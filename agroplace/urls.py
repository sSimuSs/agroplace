from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from agroplace.apps.system.views import home
from agroplace.apps.users.views import register, login
from agroplace.apps.orders.views import cart
from agroplace.apps.products.views import product, category

admin.autodiscover()
admin.site.site_header = 'AGROPLACE - ADMINISTRATION'
admin.site.site_title = 'AGROPLACE - ADMINISTRATION'

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    # path('i18n/', include('django.conf.urls.i18n')),

    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^product/(?P<pk>\d+)/$', product, name='product'),
    url(r'^category/$', category, name='category_all'),
    url(r'^category/(?P<pk>\d+)/$', category, name='category'),
    url(r'^$', home, name='home'),
    prefix_default_language=False
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
