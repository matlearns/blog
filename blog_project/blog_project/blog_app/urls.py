from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from .views import home, about_me, contact_me

urlpatterns = [
    path('', home, name='home'),
    path('/about', about_me, name='about'),
    path('/contact', contact_me, name='contact'),   
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
