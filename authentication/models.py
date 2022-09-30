from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.



class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    university = models.TextField(blank=False)

    objects = UserManager()

