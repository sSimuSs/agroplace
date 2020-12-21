from django.contrib import admin
from .models import Orders, ProductsInOrders


class ProductsInOrdersAdminInline(admin.TabularInline):
    model = ProductsInOrders
    extra = 0


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'offerings', 'total_cost', 'status', 'date']
    search_fields = ['user']
    list_filter = ['status']
    inlines = [ProductsInOrdersAdminInline]

    def offerings(self, obj):
        offerings = ProductsInOrders.objects.filter(order=obj)
        return offerings.count()