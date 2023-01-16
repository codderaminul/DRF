from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,first_name,user_name,password,**other_fields):
        other_fields.setdefault('is_staff',True),
        other_fields.setdefault('is_superuser',True),
        other_fields.setdefault('is_active',True),
        if other_fields.get('is_staff') is not True:
            raise ValueError("Supperuser must be assign is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Supperuser must be assign is_superuser=True")
        return self.create_user(email,first_name,user_name,password,**other_fields)
    def create_user(self, email, first_name, user_name, password, **other_fields):
        if not email:
            raise ValueError(_('Must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    user_name = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('abouot'),blank=True,max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']
    def __str__(self):
        return self.user_name

























