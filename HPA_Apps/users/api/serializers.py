from rest_framework import serializers
from rest_framework.authtoken.models import Token

from HPA_Apps.users.models import CustomUser,Patient,Doctor,Profile

class CreateAccountSerializer(serializers.ModelSerializer):
    choices=[('PATIENT','patient'),
             ('DOCTOR','doctor'),]



    password2=serializers.CharField(style={"type":'password'})
    type=serializers.ChoiceField(choices=choices , default='PATIENT', help_text='PATIENT or DOCTOR') #>>> do or patient
    
    class Meta:
        model=CustomUser
        fields=('email','first_name','last_name','password','password2','type')


    def save(self):

        account = CustomUser.objects.create(email=self.validated_data['email'],
                           first_name=self.validated_data['first_name'],
                           last_name=self.validated_data['last_name'],
                           type=self.validated_data['type'])
        
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!= password2:
            raise serializers.ValidationError({"password":'password doesnt match'})
        
        account.set_password(password)
          
        account.save()

        return account , self.validated_data['type']

#profile serializer

class EditingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('Location','birth_date','profile_pic')

    def save(self,token):
        

        user = Token.objects.get(key=token).user
        profile=Profile.objects.get(user=user)

        location =self.validated_data["Location"]
        birth_date=self.validated_data["birth_date"]
       
        if 'profile_pic' in self.validated_data.keys():
            profile_pic=self.validated_data['profile_pic']
            profile.profile_pic=profile_pic
        
        profile.Location=location
        profile.birth_date=birth_date
        
        
        profile.save()

