from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser,MedicalRecords

 


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

from django.forms import ModelForm
class MedicalRecordForm(ModelForm):
    class Meta:
        model=MedicalRecords
        fields='__all__'
    