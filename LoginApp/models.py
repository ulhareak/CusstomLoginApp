from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext_lazy as _
#from django.utils.translation import gettext_lazy as _

#0from phonenumber_field.model import PhoneNumberField

# Create your models here.

class UserModel(AbstractUser):
    mobile = models.CharField(max_length = 10 , unique=True , blank= True)
    #username_validator = UnicodeUsernameValidator()
    
    username =models.CharField(max_length=20 , unique=True , 
    error_messages={'unique': _("A user with that username already exists.")}) 
    password = models.CharField(_('password'), max_length=128 , blank = True)
    email = models.EmailField(max_length=20 , unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' ,'mobile' ,'first_name','password']

    objects = UserManager()

 



