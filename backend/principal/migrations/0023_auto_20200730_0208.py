# Generated by Django 3.0.8 on 2020-07-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0022_delete_imagenesmuestra'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='carousel',
            field=models.BooleanField(default=False, help_text='carousel'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='imagen_carousel',
            field=models.FileField(blank=True, null=True, upload_to='bita_archivos'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='subtitulo',
            field=models.CharField(default=1, help_text='subtitulo', max_length=255),
            preserve_default=False,
        ),
    ]