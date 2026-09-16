from django.db import models

# Create your models here.

class Condition(models.Model):
    level = models.CharField(max_length=20)

class Item(models.Model):
    name = models.CharField(max_length=120)
    cost = models.IntegerField()
    business_name = models.CharField(max_length=50)
    condition = models.ForeignKey(Condition, related_name='condition', on_delete=models.CASCADE)
    # weight = models.IntegerField(max_length=4)