from django.db import models

# Create your models here.
class Test(models.Model):
  num = models.CharField(max_length=255)
  cost = models.FloatField(max_length=255)

class Favorite(models.Model):
  stock_id = models.CharField(max_length=255, null=False)
  user_id = models.CharField(max_length=255, null=False)
  # class Meta:
  #       constraints = [
  #           models.UniqueConstraint(
  #               fields=['stock_id', 'user_id'], name='unique_migration_host_combination'
  #           )
  #       ]

class stock_info(models.Model):
  stock_id = models.CharField(max_length=255, primary_key=True)
  stock_name = models.CharField(max_length=255)
  industry = models.CharField(max_length=255)
  address = models.CharField(max_length=255, default="")
  telephone = models.CharField(max_length=255, default="")