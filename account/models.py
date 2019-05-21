from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, 'on_delete=CASCHE',unique=True)
    birth=models.DateField(blank=True,null=True)
    phone=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username
# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(User,'on_delete=CASCADE',unique=True)
    school=models.CharField(max_length=100,blank=True)
    company=models.CharField(max_length=100,blank=True)
    profession=models.CharField(max_length=100,blank=True)
    address=models.CharField(max_length=100,blank=True)
    aboutme=models.TextField(blank=True)
    photo=models.ImageField(blank=True)
    def __str__(self):
        return self.user.username
