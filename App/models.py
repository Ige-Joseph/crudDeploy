from django.db import models

# Create your models here.


class Task(models.Model):
       Title = models.CharField(max_length=100)
       decription = models.TextField(max_length=100)
       completed = models.BooleanField(default=False)
       
       def __str__(self):
            return self.Title
        
        
        
        