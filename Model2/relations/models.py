from django.db import models


class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
    
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    yazarı = models.OneToOneField(Creator, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete= models.PROTECT)

    def __str__(self):
        return self.name

class Developers(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    framework = models.ManyToManyField(Framework)

    def __str__(self):
        return self.name +" "+ self.surname