# Generated by Django 5.0.5 on 2024-06-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacore', '0005_alter_recurso_herramientas'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='direccion_ip',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recurso',
            name='password',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recurso',
            name='user',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
