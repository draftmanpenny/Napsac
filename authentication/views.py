from django.shortcuts import render
from rest_framework import generics
from .models import Account
from rest_framework import permissions
# Create your views here.



class RegistrationApiView(generics.GenericApiView):

