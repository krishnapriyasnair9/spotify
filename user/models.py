from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=12)
class Songs(models.Model):
    cover_pic = models.ImageField(upload_to="cover")
    name = models.CharField(max_length=120)
    dateofrelease= models.DateField(null=True)


class Artists(models.Model):
    name=models.CharField(max_length=120)
    DOB=models.DateField(null=True)
    bio=models.CharField(max_length=120)






