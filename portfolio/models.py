from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Carousel(models.Model):
    photo = ResizedImageField(upload_to='images/carousel/')


class Category(MPTTModel):
    name = models.CharField('category name', max_length=64)
    slug = models.SlugField('address on site')
    parent = TreeForeignKey('self', null=True, blank=True, verbose_name='parent category', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio', kwargs={'path': self.get_path()})

    def get_photos(self):
        return self.photos.all()


class Photo(models.Model):
    name = models.CharField('photo name', max_length=64, default='No name')
    parent = TreeForeignKey(Category, verbose_name='category', related_name='photos', on_delete=models.CASCADE)
    image = ResizedImageField('photo', upload_to='gallery/img/photos')

    def __str__(self):
        return self.name
