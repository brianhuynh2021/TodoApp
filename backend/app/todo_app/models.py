from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.task
    
    class Meta:
        db_table = 'todo'