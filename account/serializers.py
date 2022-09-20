from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers 
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from account.models import Accounts


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id','username','password', 'password2', 'first_name', 'last_name', 'university' )
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  , password2=validated_data['password2'], first_name=validated_data['first_name'],  last_name=validated_data['last_name'], university=validated_data['university'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'