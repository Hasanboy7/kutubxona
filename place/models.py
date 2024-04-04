from users.models import User 
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone
# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    addres=models.CharField(max_length=100)
    place_img=models.ImageField(upload_to='imgas/',null=True,blank=True)
    def __str__(self):
        return self.name

class Owner(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField()

    def __str__(self):
        return self.first_name

class PlaceOwner(models.Model):
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.place.name} owner by {self.owner}"

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    place=models.ForeignKey(Place,on_delete=models.CASCADE,related_name='izohlar')
    comment_text=models.TextField()
    stars_give=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    create_date=models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user} comment to {self.place.name} and gave {self.stars_give} stars"



class FirendRequest(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    is_accepted=models.BooleanField(default=False)