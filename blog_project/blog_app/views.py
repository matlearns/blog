from django.shortcuts import render

from django.http import HttpResponse

from .models import Blog_All

def home(request):
    return render(request, 'blog_app/home.html')

def about(request):
    return render(request, 'blog_app/about.html')

def contact(request):
    return render(request, 'blog_app/contact.html')

def test(request):
    context = Blog_All.objects.all()
    return render(request, 'blog_app/test.html', {'context' : context})        