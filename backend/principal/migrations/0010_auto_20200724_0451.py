# Generated by Django 3.0.8 on 2020-07-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20200724_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='ruta',
            field=models.CharField(blank=True, choices=[('1', 'PeliculasDetalle')], default='1', max_length=240, null=True),
        ),
    ]