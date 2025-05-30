from django.shortcuts import render
from django.http import HttpResponse
from .models import Home

def home(request):
    my_blog = Home.objects.all()
    context = {'my_blog' : my_blog}
    return render(request, "blog_app/home.html", context)

def about_me(request):
    return render(request, "blog_app/about.html")

def contact_me(request):
    return render(request, "blog_app/contact.html")