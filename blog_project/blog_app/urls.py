from django.urls import path
from .views import home, about, contact, test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('test/', test, name='test'),
    path('update/', update, name='update')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)