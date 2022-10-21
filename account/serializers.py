from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=16)
    
    class Meta: 
        model = User
        fields = '__all__'

    def validate(self, args): 
        username = args.get('username', None)
        if User.objects.filter(username=username).exists(): 
            raise serializers.ValidationError({'username:' ('Username already exists')})
        return super().validate(args)
    def create(self, validated_data): 
        return User.objects.create_account(**validated_data)
