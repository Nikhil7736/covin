from django.db import models


# Create your models here.

class booking(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)
    Repeat_Password = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
