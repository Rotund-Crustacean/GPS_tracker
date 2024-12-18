from django.db import models

# Create your models here.


class Pins(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    content = models.CharField(max_length = 10000)

