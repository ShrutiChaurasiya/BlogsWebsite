from django.db import models


# Create your models here.
class BlogModels(models.Model):
    title=models.CharField(max_length=20, blank=False)
    desc=models.TextField()

