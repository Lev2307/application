from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ChatModel
from .forms import ChatForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    form = ChatForm(request.POST or None)
    s = ChatModel.objects.all()
    return render(request, 'index.html', {'form': form, 's': s})

@login_required(login_url='/login/')
def send_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST or None)
        if form.is_valid():
            user = request.user
            text = form.cleaned_data.get('text')
            obj = ChatModel(user=user, text=text)
            obj.save()
    return redirect('index')