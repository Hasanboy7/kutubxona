from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    img=models.ImageField(upload_to='usesimg/',null=True,blank=True)
    phone_number=models.CharField(max_length=13,unique=True,null=True,blank=True)
    firends=models.ManyToManyField('users.User',blank=True)

class FriendRequest(models.Model):
    form_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='form_user')
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    is_accepted=models.BooleanField(default=False)
    
