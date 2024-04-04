from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    img=models.ImageField(upload_to='usesimg/',null=True,blank=True)
    phone_number=models.CharField(max_length=13,unique=True,null=True,blank=True)
    firends=models.ManyToManyField('users.User',blank=True)


