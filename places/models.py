from django.db import models


class Feature(models.Model):
    title             = models.CharField(max_length=255)
    imgs              = models.TextField()
    image1 = models.OneToOneField(
        "Image",
        related_name='feature1',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    image2 = models.OneToOneField(
        "Image",
        related_name='feature2',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    description_short = models.TextField()
    description_long  = models.TextField()
    coordinates_lat   = models.FloatField()
    coordinates_lng   = models.FloatField()


class Image(models.Model):
    title   = models.CharField(max_length=255)
    image   = models.ImageField()
    feature = models.ForeignKey(Feature, related_name="images", on_delete=models.CASCADE)
