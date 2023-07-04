from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='user',null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=30)
    phone = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=200)
    image = models.ImageField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class courses(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    branches = models.TextField(max_length=200)
    duration = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name





