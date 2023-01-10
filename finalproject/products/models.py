from django.db import models

class Clothing (models.Model):
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.BooleanField()

class Perfum (models.Model):
    name = models.CharField(max_length=50)
    smell = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.BooleanField()

class Ring (models.Model):
    name = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    weight = models.FloatField()
    price = models.FloatField()
    stock = models.BooleanField()        

# Create your models here.
