from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


User = settings.AUTH_USER_MODEL

class ChatModel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)