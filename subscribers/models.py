from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


User = settings.AUTH_USER_MODEL


# Create your models here.
class SubscribeModel(models.Model):
    self_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='me')
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other')