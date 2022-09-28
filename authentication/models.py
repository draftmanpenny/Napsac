from django.db import models

# Create your models here.



class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=16, blank=False, write_only=True)
    university = models.TextField(blank=False)

