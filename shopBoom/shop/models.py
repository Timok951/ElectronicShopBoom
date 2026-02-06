from django.db import models

MAX_LENGTH = 255

class Tag(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH, null=False) 

    def __str__(self):
        return self.TagName

class Company(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH, null=False)

    def __str__(self):
        return self.CompanyName
    
class Type(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH,null=False)

class Good(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH,null=False)
    amount = models.IntegerField(null=False, max_length=MAX_LENGTH)
    cost = models.FloatField(null=True, max_length=MAX_LENGTH)

    #characteristic
    max_voltage = models.IntegerField(null=True ,max_length=MAX_LENGTH)
    capacity = models.IntegerField(null=True, max_length=MAX_LENGTH)
    resistance = models.IntegerField(null=True, max_length=MAX_LENGTH)

    #Foreign keys
    article = models.ForeignKey('articles.Articles')
    type = models.ForeignKey(Type)
    company = models.ManyToManyField(Tag, models.CASCADE)

class Rate(models.Model):
    good = models.ForeignKey(Good)
    user = models.ForeignKey('users.Users')
    rating = models.FloatField(null=True, max_length=MAX_LENGTH)
    comment = models.TextField(null=True)