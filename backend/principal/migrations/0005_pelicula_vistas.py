# Generated by Django 3.0.8 on 2020-07-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20200722_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='vistas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
