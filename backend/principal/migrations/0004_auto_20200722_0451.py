# Generated by Django 3.0.8 on 2020-07-22 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20200722_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menupelicula',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mp_menu', to='principal.Menu'),
        ),
        migrations.AlterField(
            model_name='menupelicula',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mp_pelicula', to='principal.Pelicula'),
        ),
    ]