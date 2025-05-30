from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from .views import home, about_me, contact_me, user_login, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('/about', about_me, name='about'),
    path('/contact', contact_me, name='contact'),
    path('user_login/', user_login, name='user_login'),
    path('dashboard/', dashboard, name='dashboard'),   
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
