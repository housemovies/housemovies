# Generated by Django 3.0.8 on 2020-07-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_auto_20200724_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='subtitulo',
            field=models.CharField(blank=True, help_text='subtitulo', max_length=255, null=True),
        ),
    ]
