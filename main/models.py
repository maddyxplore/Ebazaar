from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class cuser(models.Model):
    Phone = models.CharField(max_length=10)
    Location = models.CharField(max_length=30)
    Address = models.CharField(max_length=250)
    user = models.OneToOneField(User,default=None,on_delete=models.CASCADE)
    
class fuser(models.Model):
    Phone = models.CharField(max_length=10)
    Location = models.CharField(max_length=30)
    Shop_no = models.CharField(max_length=20)
    user = models.OneToOneField(User,default=None,on_delete=models.CASCADE)