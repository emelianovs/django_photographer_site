import mptt_urls
from django.conf.urls import url
from django.urls import path
from . import views
#from .views import StreetGallery, WeddingGallery, PortraitGallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('portfolio/<str:path>', mptt_urls.view(model='portfolio.models.Category', view='portfolio.views.category', slug_field='slug'), name='portfolio'),
    url(r'^portfolio/(?P<path>.*/)', mptt_urls.view(model='portfolio.models.Category', view='portfolio.views.category', slug_field='slug'), name='portfolio'),
                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
