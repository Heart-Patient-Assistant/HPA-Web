from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes User Profile Object"""
    class Meta:
        model = models.CustomUser
        fields = ('id','email','password','first_name','last_name')
        exta_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}
            }
        }

    def create(self,validated_data):
        """Create and return a new user"""
        user = models.CustomUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user
