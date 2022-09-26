from typing_extensions import Required
from django.db import models

# Create your models here.

class Accounts(models.Model): 
    id = models.IntegerField(primary_key=True)
    university = models.TextField(blank=False)
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    username = models.CharField(max_length=20,blank=False, unique=True)
    password = models.CharField(max_length=16, blank=False)
    password2 = models.CharField(max_length=16, blank=False)
