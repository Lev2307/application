from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# Create your views here.
def registration_view(request):
    p = UserProfile
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        p = UserProfile(profile=user)
        p.save()
        return redirect("/")
    return render(request, 'accounts/registration_form.html', {'form': form})
