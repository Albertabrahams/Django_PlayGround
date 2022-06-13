from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField()
    TITLE = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    )
    priority = models.CharField(max_length=1, choices=TITLE, default="M")
    done = models.BooleanField()
    updateDate = models.DateTimeField(auto_now_add=True)
    createDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

