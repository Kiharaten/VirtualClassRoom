from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    gender = models.IntegerField(default=0)
    birthday = models.DateField('date birthday')
    profile = models.CharField(max_length=255)

class ClassRoom(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    subject = models.IntegerField(default=0)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    length = models.IntegerField(default=30)



