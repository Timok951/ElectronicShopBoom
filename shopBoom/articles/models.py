from django.db import models

MAX_LENGTH = 255

class Article (models.Model):
    name = models.TextField(unique=True)
    text = models.TextField()
    image = models.ImageField()

