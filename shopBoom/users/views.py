from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

def login_user(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return profile_page(request)
        
    return render(request, 'auth/login.html', {'form':form})

def registration_user(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    return render(request, 'auth/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')

def profile_page(request):
    return render(request, "profile/profile.html")
            