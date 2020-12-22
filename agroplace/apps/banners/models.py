from django.db import models
from agroplace.functions import get_random_code


def main_banners_images_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    imagename = get_random_code(6).lower()
    # file will be uploaded to MEDIA_ROOT/images/<product_id>/<filename>
    return 'main_banners/{0}/{1}'.format(instance.id, '{}.{}'.format(imagename, ext))


class MainBanners(models.Model):
    image = models.ImageField(upload_to=main_banners_images_directory_path)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    link = models.URLField(default="/")
    status = models.BooleanField(default=True)
