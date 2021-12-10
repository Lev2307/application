from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm, LoginForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration_view(request):
    p = UserProfile
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password, is_staff=False)
        user.save()
        p = UserProfile(profile=user)
        p.save()
        return redirect("/")
    return render(request, 'accounts/registration_form.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username_login = form.cleaned_data.get('username')
        password_login = form.cleaned_data.get('password')
        user = authenticate(request, username=username_login, password=password_login)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/login/")
    return render(request, 'accounts/login_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login/")
def profile_view(request):
    user = request.user
    return render(request, "accounts/profile.html", {'profile': user})
