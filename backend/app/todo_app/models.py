from django.db import models

# Create your models here.

class Task(models.Model):
    newTask = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timeAdded = models.DateTimeField(auto_now_add=True)
    editing = models.BooleanField(default=False)
    lastEdited = models.CharField(max_length=255, blank=True)
