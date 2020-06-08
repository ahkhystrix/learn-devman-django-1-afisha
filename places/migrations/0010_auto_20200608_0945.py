# Generated by Django 3.0.7 on 2020-06-08 06:45

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20200608_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'verbose_name': 'Активность', 'verbose_name_plural': 'Активности'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('position'), nulls_last=True)], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='feature',
            name='coordinates_lat',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='coordinates_lng',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description_long',
            field=models.TextField(verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description_short',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='placeId',
            field=models.CharField(max_length=255, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Позиция'),
        ),
    ]