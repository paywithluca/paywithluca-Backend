# from pyexpat import model
from rest_framework import serializers
from .models import *
from .models import CustomUser



class RegisterationSerializer(serializers.ModelSerializer):
    
    
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username','department', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
        
    # overiding the default save method
    def save(self):
        account = CustomUser(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            department = self.validated_data['department'],
        
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        # checking if the first password equals the second password
        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})
        
        
        # checking if the email of a user already exists
        elif CustomUser.objects.filter(email = account.email).exists():
            raise serializers.ValidationError({'email': 'User with this Email Already Exists'})
        
        account.set_password(password)
        account.save()
        return account
    
    
