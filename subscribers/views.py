from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SubscribeModel
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def subs(request, **kwargs):
    if request.method =="POST":
        self_user = request.user
        other_user = get_object_or_404(User, id=kwargs['pk'])
        if self_user != other_user and not SubscribeModel.objects.filter(self_user=self_user, other_user=other_user).exists():
            sub_model = SubscribeModel(self_user=self_user, other_user=other_user)
            sub_model.save()

    return redirect('index')
