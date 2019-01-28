from django.db import models
from projects.models import Project 

# python manage.py makemigrations
# Create your models here.
class Repo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    values = models.TextField(blank=True)
    def __str__(self): 
        return self.name