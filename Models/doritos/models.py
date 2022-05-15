from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mature = models.BooleanField()