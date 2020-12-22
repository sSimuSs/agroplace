from django.db import models
from agroplace.functions import get_random_code


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
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
