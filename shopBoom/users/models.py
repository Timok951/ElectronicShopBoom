from django.db import models
from django.contrib.auth.models import AbstractUser

MAX_LENGTH = 255

class Role(models.Model):
    rolename = models.CharField(unique=True, max_length=MAX_LENGTH)
    
    def __str__(self):
        return self.rolename

#Best way to create your user
class User(AbstractUser):
    
    humanname = models.CharField(unique=True, null=True, max_length=MAX_LENGTH,blank=True)
    email = models.EmailField(unique=True, null=True, max_length=MAX_LENGTH, blank=True)
    phonenumber = models.CharField(unique=True, null=True, max_length=14, blank=True)
    address = models.TextField(unique=False, null=True, blank=True)    
    bonus = models.DecimalField(null=False, default=0.0, decimal_places=2, max_digits=10)
    role = models.ForeignKey( Role, on_delete=models.SET_NULL, null=True, blank=True)
    
    favorites = models.ManyToManyField(
        'shop.Good',
        through="Favorites",
        through_fields=("user", "good")
    )
    
    def __str__(self):
        return self.username

#to try define own many to manyField
class UserFavorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    good = models.ForeignKey('shop.Good', on_delete=models.CASCADE, null=False)
