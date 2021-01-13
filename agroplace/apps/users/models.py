from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager


class Users(AbstractUser):

    username = None
    phone = models.CharField(max_length=28, unique=True, verbose_name=_('Phone'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('Email'))
    address = models.TextField(blank=True, null=True, verbose_name=_('Address'))

    objects = UserManager()

    REQUIRED_FIELDS = ('email', )
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
