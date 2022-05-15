from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    
class Product(models.Model):
    surname = models.CharField(max_length=20)