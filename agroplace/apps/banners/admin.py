from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.admin.widgets import AdminFileWidget
from .models import MainBanners


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


@admin.register(MainBanners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ['id', 'banner_image', 'title', 'status']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ['title', 'sub_title']
    list_per_page = 20
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def banner_image(self, obj):
        if obj.image:
            return format_html(
                "<img src='" + obj.image.url + "' style='max-width:100px;max-height:70px'>")
        else:
            return "---"
