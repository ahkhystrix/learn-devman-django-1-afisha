from django.db import models


class Feature(models.Model):
    title             = models.CharField(max_length=255)
    imgs              = models.TextField()
    description_short = models.TextField()
    description_long  = models.TextField()
    coordinates_lat   = models.FloatField()
    coordinates_lng   = models.FloatField()
