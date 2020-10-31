from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.


############# ModelManager
class CustomUserManager(BaseUserManager):

    ### Custom user model where (((field = email))) is the unique identifier
    ### for authentication
    def create_user(self,email,password, **extra_fields):
        ### Create and save User in DB with the given email and password
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password, **extra_fields):
        ### Create and save SuperUser in DB with the given email and password

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super User must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super User must have is_superuser=True.'))
        return self.create_user(email,password, **extra_fields)

############# User Model
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
