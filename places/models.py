from django.db import models
from django.db.models import F


class Feature(models.Model):
    placeId = models.CharField(max_length=255, verbose_name="Идентификатор")
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = models.TextField(verbose_name="Краткое описание")
    description_long = models.TextField(verbose_name="Полное описание")
    coordinates_lat = models.FloatField(verbose_name="Долгота")
    coordinates_lng = models.FloatField(verbose_name="Широта")

    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = "Активности"

    def __str__(self):
        return self.title


class Image(models.Model):
    position = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        verbose_name="Позиция"
    )
    image = models.ImageField(verbose_name="Картинка")
    feature = models.ForeignKey(
        Feature,
        related_name="images",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = [F('position').asc(nulls_last=True)]
