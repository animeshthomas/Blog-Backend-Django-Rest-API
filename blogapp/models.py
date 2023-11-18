from django.db import models

# Create your models here.
class blogAdd(models.Model):
    userid = models.CharField(default="",max_length=100)
    title = models.CharField(default="",max_length=100)
    message = models.CharField(default="",max_length=1000)


class registration(models.Model):
    name=models.CharField(default="",max_length=100)
    profile=models.TextField(default="")
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)