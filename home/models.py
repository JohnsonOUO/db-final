from django.db import models
from login.models import User
# Create your models here.

class Test(models.Model):
  num = models.CharField(max_length=255)
  cost = models.FloatField(max_length=255)

class stock_info(models.Model):
  stock_id = models.CharField(max_length=255, primary_key=True)
  stock_name = models.CharField(max_length=255)
  industry = models.CharField(max_length=255)
  address = models.CharField(max_length=255, default="")
  telephone = models.CharField(max_length=255, default="")

class Favorite(models.Model):
  stock_id = models.ForeignKey(stock_info, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  # class Meta:
  #       constraints = [
  #           models.UniqueConstraint(
  #               fields=['stock_id', 'user_id'], name='unique_migration_host_combination'
  #           )
  #       ]

