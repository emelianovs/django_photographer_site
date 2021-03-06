from django.urls import path
from .views import ReviewsList, ReviewAdd, ContactPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reviews/', ReviewsList.as_view(), name='reviews'),
    path('add_review/', ReviewAdd.as_view(), name='review-add'),
    path('contacts/', ContactPage.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
