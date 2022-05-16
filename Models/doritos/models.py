from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mature = models.BooleanField()

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.mature)

class Customer2(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mature = models.BooleanField()

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.mature)