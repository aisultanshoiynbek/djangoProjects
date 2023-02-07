from django.db import models

# Create your models here.

class User (models.Model):
    name =  models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
