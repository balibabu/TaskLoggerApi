from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.CharField(max_length=50, default='others')
    tags = models.CharField(max_length=20)
    createdTime = models.DateTimeField(auto_now_add=True)
    modifiedTime = models.DateTimeField(auto_now=True)