from django.db import models
from django_resized import ResizedImageField


class Gallery(models.Model):
    photo = ResizedImageField(upload_to='images/')

    class Meta:
        abstract = True


class Street(Gallery):
    photo = ResizedImageField(upload_to='images/street/')


class Wedding(Gallery):
    photo = ResizedImageField(upload_to='images/wedding/')


class Portrait(Gallery):
    photo = ResizedImageField(upload_to='images/portrait/')


class Carousel(Gallery):
    photo = ResizedImageField(upload_to='images/carousel/')
