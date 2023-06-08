from django.db import models

# Create your models here.
class Test(models.Model):
  num = models.CharField(max_length=255)
  cost = models.FloatField(max_length=255)

class Favorite(models.Model):
  num = models.CharField(max_length=255)
  cost = models.FloatField(max_length=255)