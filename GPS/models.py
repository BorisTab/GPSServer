from django.db import models

# Create your models here.
class Coordinates(models.Model):
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
