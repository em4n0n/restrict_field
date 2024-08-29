from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.Charfield(max_length=10)
    
