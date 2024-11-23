from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm



def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Home - Авторизация',
        'form': form

    }
    return render(request, 'users/login.html', context)

def registration(request):


    context = {
        'title': 'Home - Главная',
        'content':'Магазин мебели HOME',   
    }
    return render(request, 'users/registration.html', context)

def profile(request):


    context = {
        'title': 'Home - Главная',
        'content':'Магазин мебели HOME',   
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    context = {
        'title': 'Home - Главная',
        'content':'Магазин мебели HOME',   
    }
    return render(request, 'users/profile.html', context)