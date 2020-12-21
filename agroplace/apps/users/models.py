from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Users(AbstractUser):

    username = None
    phone = models.CharField(max_length=28, unique=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    objects = UserManager()

    REQUIRED_FIELDS = ('email', )
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
