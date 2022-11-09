from django.db import models

# Create your models here.
class TodoModel(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return "task={0}, description={1}, status={2} ".format( self.task,self.description,self.status)
