from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django import forms
from django.forms import widgets
from django.forms.widgets import Select
from .models import User, Profile, MedicalRecords, appointment
from django.forms import ModelForm

choices = [
    ("Allergy and immunology", "Allergy and immunology"),
    ("Anesthesiology", "Anesthesiology"),
    ("Dermatology", "Dermatology"),
    ("Diagnostic radiology", "Diagnostic radiology"),
    ("Neurology", "Neurology"),
    ("Pathology", "Pathology"),
    ("Pediatrics", "Pediatrics"),
    ("Surgery", "Surgery"),
]
choices_list = []
for item in choices:
    choices_list.append(item)


class ProfilePageForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}), required=False
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "email",
            "bio",
            "profile_pic",
            "facebook_url",
            "twitter_url",
            "instagram_url",
        )
        widgets = {
            "bio": forms.Textarea(
                attrs={"class": "form-control", "rows": 2, "cols": 10}
            ),
        }


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "cols": 5}),
        required=False,
    )
    facebook_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    twitter_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    instagram_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "email",
            "bio",
            "profile_pic",
            "facebook_url",
            "twitter_url",
            "instagram_url",
        )


class DoctorPageForm(forms.ModelForm):
    academic_Title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    employment_history = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "cols": 10}),
        required=False,
    )
    experience = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "cols": 10}),
        required=False,
    )
    speciality = forms.MultipleChoiceField(
        label=u"Select Your Specialities",
        choices=choices_list,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
    #

    class Meta:
        model = Profile
        fields = (
            "academic_Title",
            "employment_history",
            "experience",
            "speciality",
        )


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
        fields = ("old_password", "new_password 1", "new_password 2")


# ----------------------------
class MedicalRecordForm(ModelForm):
    class Meta:
        model = MedicalRecords
        fields = "__all__"

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = appointment
        fields = '__all__'
        widgets = {

            "patient": forms.HiddenInput(),

        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if self.instance:
            # self.fields['patient'].queryset = User.objects.filter(user_type="P")
            self.fields['doctor'].queryset = User.objects.filter(type="DOCTOR")
            self.fields["date"].label = "Date (YYYY-MM-DD)"
            self.fields["time"].label = "Time 24 hr (HH:MM)"

