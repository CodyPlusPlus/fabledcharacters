from django.db import models

# Create your models here.
class Obituary(models.Model):
    name    = models.CharField(max_length=50) # remember that max_length is required for CharField
    system  = models.CharField(max_length=50, blank=True, null=True)
    level   = models.PositiveSmallIntegerField()
    story   = models.CharField(max_length=280)

# remember to makemigrations and migrate whenever you modify this file