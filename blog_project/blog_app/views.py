from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user:
                return redirect('home')
        else:
            messages.error(request, 'Invalide username or password.')

    return render(request, "cms/login.html")
