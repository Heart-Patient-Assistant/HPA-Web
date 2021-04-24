from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Patient, Doctor, Profile, Feedback, MedicalRecords
from .forms import UserCreationForm, UserChangeForm

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = (
        "email",
        "is_active",
    )
    list_filter = (
        "email",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name", "type")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "type",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Patient)
class PatientAdmin(UserAdmin):
    readonly_fields = ("type",)


@admin.register(Doctor)
class DoctorAdmin(UserAdmin):
    readonly_fields = ("type",)


admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(MedicalRecords)
