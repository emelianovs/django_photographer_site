from django.shortcuts import render
from django.views.generic import ListView

from .models import Street, Wedding, Portrait, Carousel


def home(request):
    image = Carousel.objects.all()
    return render(request, 'portfolio/home.html', {"image": image})


def about(request):
    return render(request, 'portfolio/about.html')


class StreetGallery(ListView):
    model = Street
    context_object_name = 'streets'


class WeddingGallery(ListView):
    model = Wedding
    context_object_name = 'weddings'


class PortraitGallery(ListView):
    model = Portrait
    context_object_name = 'portraits'
