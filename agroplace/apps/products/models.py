from django.db import models
from agroplace.functions import get_random_code


def cats_banner_images_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    imagename = get_random_code(6).lower()
    # file will be uploaded to MEDIA_ROOT/images/<product_id>/<filename>
    return 'cats_images/{0}/{1}'.format(instance.id, '{}.{}'.format(imagename, ext))


class Categories(models.Model):
    name = models.CharField(max_length=250)
    banner_image = models.ImageField(upload_to=cats_banner_images_directory_path)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


def products_images_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    imagename = get_random_code(6).lower()
    # file will be uploaded to MEDIA_ROOT/images/<product_id>/<filename>
    return 'products/{0}/{1}'.format(instance.id, '{}.{}'.format(imagename, ext))


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost = models.FloatField()
    image = models.ImageField(upload_to=products_images_directory_path)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
