from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from .models import Home
from django.contrib.auth.decorators import login_required




def home(request):
    my_blog = Home.objects.all()
    context = {'my_blog' : my_blog}
    return render(request, "blog_app/home.html", context)

def about_me(request):
    return render(request, "blog_app/about.html")

def contact_me(request):
    return render(request, "blog_app/contact.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalide username or password.')

    return render(request, "cms/login.html")


@login_required
def dashboard(request):
    if request.method == 'POST':
         title = request.POST.get('title')
         author = request.POST.get('author')
         post_on = request.POST.get('post_on')
         image = request.FILES.get('image')
         content = request.POST.get('content')
         Home.objects.create(
              title = title,
              author = author,
              post_on = post_on,
              image = image,
              content = content,
         )

    
    return render(request, "cms/dashboard.html")