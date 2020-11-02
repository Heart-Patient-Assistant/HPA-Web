from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password, **extra_fields):
        ### Create and save SuperUser in DB with the given email and password

        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super User must have is_superuser=True.'))
        return self.create_user(email,password, **extra_fields)

############# User Model
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'),default=True)
    date_joined = models.DateTimeField(_('date joined'),default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('CustomUser')
        verbose_name_plural = _('CustomUsers')

    def __str__(self):
        return self.email

        # Return Full name with a space between them
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

        # Send an E-mail to the user
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

############# User Profile
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    #phone_number= ..
    birth_date = models.DateField(null=True,blank=True)
    Location = models.CharField(max_length=30,blank=True)
    #profile= models.ImageField(null=True,bland=True)
    #doctor_resp = ..


########### Receiver to create/update when create/update user instance
@receiver(post_save,sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



############# User Model 2
class Patient(CustomUser):
    objects = CustomUserManager()
    class Meta:
        proxy = True
        #ordering = ('..')

    #def some_function(self):

class Doctor(CustomUser):
    objects = CustomUserManager()
    class Meta:
        proxy = True
        #ordering = ('..')

    #def some_function(self):
