from django.contrib import admin
from .models import Street, Wedding, Portrait, Carousel


admin.site.register(Street)
admin.site.register(Wedding)
admin.site.register(Portrait)
admin.site.register(Carousel)


admin.site.site_header = "Photographer's portfolio"
