from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)
    deadline = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title + self.description