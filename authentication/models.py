from django.db import models
from django.contrib.auth.models import UserManager
from django.forms import IntegerField

# Create your models here.



class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    university_id = models.ForeignKey('University',
                     on_delete=models.PROTECT, blank=False)

    objects = UserManager()



class University(models.Model):
    UCLA = 'University of Californa'
    USC = 'University of Southern California'
    HIU = 'Hope International University'
    CSUF = 'Cal State Fullerton'


    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)





