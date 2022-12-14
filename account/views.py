from django.shortcuts import render
from rest_framework import generics


from account import serializers


from rest_framework import permissions
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.



class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer 

    def post(self, request): 
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message": "User created successfully",
                "Users": serializer.data}, status=status.HTTP_201_CREATED) 
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST) 


class UserBookShelfAPI(APIView):
    pass 