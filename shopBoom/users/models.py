from django.db import models
from django.contrib.auth.models import AbstractUser
MAX_LENGTH = 255

# Create your models here.
class Role(models.Model):
    rolename = models.CharField(unique=True, max_length=MAX_LENGTH)
    
    def __str__(self):
        return self.rolename

class User(AbstractUser):
    
    humanname = models.CharField(unique=True, null=True, max_length=MAX_LENGTH,blank=True)
    email = models.EmailField(unique=True, null=True, max_length=MAX_LENGTH, blank=True)
    phonenumber = models.CharField(unique=True, null=True, max_length=14, blank=True)
    address = models.TextField(unique=False, null=True, blank=True)    
    bonus = models.DecimalField(null=False, default=0.0, decimal_places=2, max_digits=10)
    role = models.ForeignKey( Role, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username