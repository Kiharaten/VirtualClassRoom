from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.IntegerField(default=0)
    birthday = models.DateField('date birthday')
    email = models.CharField(max_length=100)