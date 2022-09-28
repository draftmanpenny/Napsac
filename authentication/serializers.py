from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, blank=False, unique=True)
    password = serializers.CharField(max_length=16, blank=False, write_only=True)
    
    class meta: 
        model = Account
        fields = '__all__'

    def validate(self, args): 
        username = args.get('username', None)
        if Account.objects.filter(username=username).exists(): 
            raise serializers.ValidationError({'username:' ('Username already exists')})
        return super().validate(args)
    def create(self, validated_data): 
        return Account.objects.create_account(**validated_data)
