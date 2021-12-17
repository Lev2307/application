from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ChatModel
from .forms import ChatForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    form = ChatForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
    return render(request, 'index.html', {'form': form})

@login_required(login_url='/login/')
def message(request):
    return redirect('index')