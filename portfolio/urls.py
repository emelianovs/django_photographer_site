from django.urls import path
from . import views
from .views import StreetGallery, WeddingGallery, PortraitGallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/street/', StreetGallery.as_view(), name='street'),
    path('gallery/wedding/', WeddingGallery.as_view(), name='wedding'),
    path('gallery/portrait/', PortraitGallery.as_view(), name='portrait')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
