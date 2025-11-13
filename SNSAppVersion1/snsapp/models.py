from django.db import models

# Create your models here.
class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    images = models.ImageField(upload_to='', blank=True, null=True)
    views = models.IntegerField(default=0)
    subscribe = models.BooleanField(default=False)
    good = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)