from django.db import models
from django.contrib.auth.models import UserManager
from django.forms import IntegerField

# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=100, blank=False)

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)



class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    password = models.CharField(max_length=16, blank=False)
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    

    object = UserManager()


class UserBookShelf(models.Model):
    user = models.OneToOneField(Users, on_delete=models.PROTECT, primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

