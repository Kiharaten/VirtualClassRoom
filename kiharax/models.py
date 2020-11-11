import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

    # name        -> /kiharax/name/
    # gender      -> /kiharax/gender/
    # age         -> /kiharax/age/
    # height      -> /kiharax/height/
    # weight      -> /kiharax/weight/
    # description -> /kiharax/description/

class UserParameter(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

class UserDescription(models.Model):
    user = models.ForeignKey(UserParameter, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datepublished')

    def __str__(self):
        return self.description

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

