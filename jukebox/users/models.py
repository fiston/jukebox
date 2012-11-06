from django.db import models
from django.contrib.auth.models import User


class RecoveryToken(models.Model):
    email = models.EmailField(max_length=75,)
    token = models.CharField(max_length=32, unique=True, default=None, help_text="token to reset password")
    created_on = models.DateTimeField(auto_now_add=True,)
