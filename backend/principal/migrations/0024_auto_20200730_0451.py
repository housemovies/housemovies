# Generated by Django 3.0.8 on 2020-07-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0023_auto_20200730_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='subtitulo',
            field=models.CharField(blank=True, help_text='subtitulo', max_length=255, null=True),
        ),
    ]
