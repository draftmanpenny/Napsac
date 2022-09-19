from django.db import models

# Create your models here.


class UCLA(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class UCSB(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class Stanford(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class MIT(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class Howard(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class FSU(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class USC(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class BostonU(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)

class Berkley(models.Model):
    instructor = models.CharField(max_length=100)
    textbook = models.CharField(max_length=None)
    course = models. CharField(max_length= 100)
