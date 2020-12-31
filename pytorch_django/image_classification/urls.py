from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'image_classification'

urlpatterns = [
    path('', TemplateView.as_view(template_name='image_classification/index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
