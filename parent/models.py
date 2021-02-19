from django.db import models

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    gender = models.IntegerField(default=0)
    birthday = models.DateField('date birthday')

    def __str__(self):
        return self.name