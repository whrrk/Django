from django.db import models

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY,
    )

    duedate = models.DateTimeField()
    
    def __str__(self):
        return self.title