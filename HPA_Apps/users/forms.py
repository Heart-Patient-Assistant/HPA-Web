from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django import forms
from .models import User, Profile, MedicalRecords
from django.forms import ModelForm


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic", "website_url")
        widgets = {
            "bio": forms.Textarea(
                attrs={"class": "form-control", "rows": 2, "cols": 10}
            ),
            # 'profile_pic': forms.TextInput(attrs={'class':'form-control'}),
            "website_url": forms.TextInput(attrs={"class": "form-control"}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        # fields = ('username','first_name','last_name','email','password1','password2')
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    # username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        # fields = ('username','first_name','last_name','email','password')
        fields = ("first_name", "last_name", "email", "password")


class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password1 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")


# ----------------------------
class MedicalRecordForm(ModelForm):
    class Meta:
        model = MedicalRecords
        fields = "__all__"
