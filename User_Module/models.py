from django.db import models

# Create your models here.
class UserRegistrationModel(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150,unique=True)
    contactno=models.IntegerField(unique=True)
    password=models.CharField(max_length=100)
