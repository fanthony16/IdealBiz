from django.db import models
from datetime import date
from django.contrib.auth.models import User
from PIL import Image

class userGroup(models.Model):
    txtGroupCode =models.CharField(max_length=20)
    txtGroupName = models.CharField(max_length=200)
    dteCreated = models.DateField(default=date.today)
    
    def __str__(self) :
        return self.txtGroupName

class userProfile(models.Model):
    txtUser = models.OneToOneField(User, on_delete= models.CASCADE)
    txtUserAccessGroup = models.OneToOneField(userGroup,null=True,on_delete=models.SET_NULL)
    dteCreated = models.DateField(default=date.today)
    image = models.ImageField(default="default.jpg", upload_to = "profile_pics")

    def __str__(self) -> str:
        return self.txtUser.username

# Create your models here.
