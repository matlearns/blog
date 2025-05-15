from django.shortcuts import render

from django.http import HttpResponse

from .models import Blog_All, About_Me

def home(request):
    context = Blog_All.objects.all()
    return render(request, 'blog_app/home.html', {'context' : context})

def about(request):
    about = About_Me.objects.all()
    return render(request, 'blog_app/about.html', {'context' : about})

def contact(request):
    return render(request, 'blog_app/contact.html')

def test(request):
    context = Blog_All.objects.all()
    return render(request, 'blog_app/test.html', {'context' : context})        