from django.db import models
from django.contrib.auth.models import UserManager




# Create your models here.



class University(models.Model):
    name =  models.CharField(max_length=100)




class Books(models.Model): 
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=100, blank=False)  # should have something to do with AWS server 


class UCLA(models.Model):
    name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)


class HIU(models.Model):
    name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)


class UCI(models.Model):
    name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)

class CSUF(models.Model):
    name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)

class USC(models.Model):
    name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    books = models.ForeignKey(Books,  on_delete=models.CASCADE)




class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    # every user needs a book shelf refrence  


    objects = UserManager()





class BookShelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    books =  models.ForeignKey(Books,  on_delete=models.CASCADE)
    




