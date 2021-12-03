from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)

