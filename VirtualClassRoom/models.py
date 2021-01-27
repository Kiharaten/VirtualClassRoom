from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

