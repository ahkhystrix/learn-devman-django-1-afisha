# Generated by Django 3.0.7 on 2020-06-08 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200608_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='imgs',
        ),
    ]