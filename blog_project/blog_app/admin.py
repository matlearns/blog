from django.contrib import admin


# Register your models here.
from .models import Blog_All, About_Me

admin.site.register(Blog_All)
admin.site.register(About_Me)