# Generated by Django 3.0.8 on 2020-07-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20200724_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='ruta',
            field=models.CharField(blank=True, choices=[('1', 'home'), ('2', 'MenusAdministrar')], default='2', max_length=240, null=True),
        ),
    ]