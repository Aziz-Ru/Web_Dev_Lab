from django.db import models

# Create your models here.
class user(models.Model):
    username    =models.CharField(max_length=100)
    email       =models.CharField(max_length=200)
    password    =models.CharField(max_length=200)
    birthdate   =models.CharField(max_length=20)
