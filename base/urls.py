from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from base import views

urlpatterns = [
    path('', views.home),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
