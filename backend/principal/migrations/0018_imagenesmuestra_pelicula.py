# Generated by Django 3.0.8 on 2020-07-25 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0017_auto_20200725_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenesmuestra',
            name='pelicula',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagen_pelicula', to='principal.Pelicula'),
            preserve_default=False,
        ),
    ]
