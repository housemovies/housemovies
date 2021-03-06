# Generated by Django 3.0.8 on 2020-07-24 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0015_busquedas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('delete', models.DateTimeField(blank=True, default=None, help_text='Date time on which the object was last delete.', null=True, verbose_name='delete at')),
                ('texto', models.CharField(blank=True, max_length=240, null=True)),
                ('uc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='busqueda_created', related_query_name='busquedas', to=settings.AUTH_USER_MODEL)),
                ('um', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='busqueda_update', related_query_name='busquedas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'principal_busquedas',
                'ordering': ['-created', '-modified'],
            },
        ),
        migrations.DeleteModel(
            name='Busquedas',
        ),
    ]
