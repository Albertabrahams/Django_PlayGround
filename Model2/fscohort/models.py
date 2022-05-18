from django.db import models

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", 'Freshman'),
        ("SP", 'Sophomore'),
        ("JR", 'Junior'),
        ("SR", 'Senior'),
        ("GRD", 'Graduate'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='media/%Y/%m/%d/')
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    birt_date = models.DateField()
    year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, default="FR")

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Öğrenciler"