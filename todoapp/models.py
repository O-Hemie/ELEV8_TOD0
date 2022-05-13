from django.db import models

# Create your models here.
class Task(models.Model):
    ''' Creating a task table in my database'''
    name=models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id'] 