from rest_framework import serializers
from django.db.models import fields
from rest_framework import serializers

from HPA_Apps.users.models import CustomUser,Profile,Doctor

class CreateAccountSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"type":'password'})
    type=serializers.CharField(max_length=20, required=False) #>>> do or patient
    
    class Meta:
        model=CustomUser
        fields=('email','first_name','last_name','password','password2','type')


    def save(self):
        
        #if self.validated_data['email']=='patient' 
        account=CustomUser(email=self.validated_data['email'],
                           first_name=self.validated_data['first_name'],
                           last_name=self.validated_data['last_name'])
        
        #if self.validated_data['email']=='doctor' 
            #account=Doctor(email=self.validated_data['email'],
            #               first_name=self.validated_data['first_name'],
            #               last_name=self.validated_data['last_name'])
        
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!= password2:
            raise serializers.ValidationError({"password":'password doesnt match'})
        
        account.set_password(password)
          
        account.save()

        return account