from django.db import models

# Create your models here.

class Condition(models.Model):
    level = models.CharField(max_length=20)

class Business(models.Model):
    name = models.CharField(max_length=50)

class Item(models.Model):
    name = models.CharField(max_length=120)
    business_name = models.ForeignKey(Business, related_name='business', on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, related_name='condition', on_delete=models.CASCADE)
    price = models.IntegerField()
    # weight = models.IntegerField(max_length=4)