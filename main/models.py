from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    First_name = models.CharField(max_length=100)
    Second_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    Password = models.CharField(max_length=200)
    Location = models.CharField(max_length=30)
    Address = models.CharField(max_length=250)
    Shop_no = models.CharField(max_length=20)
    is_farmer = models.BooleanField(default=False)
