from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from .models import Products
from django.contrib.admin.widgets import AdminFileWidget


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, **kwargs):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                ' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: contain;"/></a> %s ' % \
                (image_url, image_url, file_name, ''))

        output.append(super(AdminFileWidget, self).render(name, value, attrs, ))
        return u''.join(output)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_image', 'name', 'cost', 'status', 'date']
    list_editable = ['status', 'cost']
    list_display_links = ['name']
    list_per_page = 20
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def product_image(self, obj):
        if obj.image:
            return format_html(
                "<img src='" + obj.image.url + "' style='max-width:100px;max-height:70px'>")
        else:
            return "---"

