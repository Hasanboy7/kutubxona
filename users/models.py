from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    img=models.ImageField(upload_to='usesimg/')
    phone_number=models.CharField(max_length=13,unique=True,null=True,blank=True)