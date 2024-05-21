from django.shortcuts import render, redirect
from main.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from main.models import Slide


def index(request):
    slides = Slide.objects.all()
    return render(request, 'main/index.html', context={'slides':slides})

def account(request):
    if request.method == 'POST':
        auth_form = AuthFormCustom(request, data=request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data.get('username')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')

    auth_form = AuthFormCustom()
    reg_form = RegisterFormCustom()

    return render(request, 'main/signin.html', context={'reg_form':reg_form, 'auth_form':auth_form})

def create_account(request):
    if request.method == 'POST':
        reg_form = RegisterFormCustom(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data.get('username')
            email = reg_form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Данное имя уже занято')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Данный email уже занят')
            else:
                user = reg_form.save(commit=False)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                login(request, user)
                return redirect('index')
            
def user_logout(request):
    logout(request)
    return redirect('index')
