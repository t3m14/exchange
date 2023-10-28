from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=30)
    balance_usd = models.FloatField(default=0)
    balance_rdw = models.FloatField(default=0)
 