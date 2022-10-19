from turtle import title
from django.db import models

# Create your models here.


class Books(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=False)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=100)