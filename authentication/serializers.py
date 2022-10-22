from rest_framework import serializers
from authentication.models import Users


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=16)
    
    class Meta: 
        model = Users
        fields = '__all__'

    def validate(self, args): 
        username = args.get('username', None)
        if Users.objects.filter(username=username).exists(): 
            raise serializers.ValidationError({'username:' ('Username already exists')})
        return super().validate(args)
    def create(self, validated_data): 
        return Users.objects.create_account(**validated_data)
