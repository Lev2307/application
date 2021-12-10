from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())