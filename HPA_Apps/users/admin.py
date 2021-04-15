from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,Patient,Doctor,Profile,Feedback,MedicalRecords
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email','is_active',)
    list_filter = ('email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','type','first_name','last_name')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Patient)
class PatientAdmin(CustomUserAdmin):
    readonly_fields = ('type',)

@admin.register(Doctor) 
class DoctorAdmin(CustomUserAdmin):
    readonly_fields = ('type',)

admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(MedicalRecords)