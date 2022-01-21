from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ChatModel
from .forms import ChatForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from subscribers.models import SubscribeModel

# Create your views here.

def index(request):
    form = ChatForm(request.POST or None)
    s = ChatModel.objects.all()

    filter_user = int(request.GET.get('filter', 0))
    sub = request.GET.get('sub', False)

    only_subs = SubscribeModel.objects.filter(self_user__id=request.user.id)
    messages = ChatModel.objects.filter(user__id=filter_user) or ChatModel.objects.all()
    
    if sub:
        messages = messages.filter(user_id__in=[user.other_user.id for user in only_subs])
    return render(request, 'index.html', {'form': form, 's': s, 'chat': messages})  

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