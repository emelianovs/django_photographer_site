from django.contrib import admin
#from .models import Street, Wedding, Portrait, Carousel
from .models import Category, Carousel, Photo

'''admin.site.register(Street)
admin.site.register(Wedding)
admin.site.register(Portrait)'''
admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Photo)

admin.site.site_header = "Photographer's portfolio"
