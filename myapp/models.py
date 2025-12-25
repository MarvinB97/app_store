from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Tasks(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    cantidad = models.IntegerField()
    project = models.ForeignKey(Project, on_delete= models.CASCADE)