from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import Users


@admin.register(Users)
class UsersAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    ordering = ['-id']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    list_display = ['id', 'first_name', 'phone', 'date_joined', 'is_active']