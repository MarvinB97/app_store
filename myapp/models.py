from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tasks(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    cantidad = models.IntegerField()
    project = models.ForeignKey(Project, on_delete= models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name