# Generated by Django 5.1.5 on 2025-01-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_terminales', '0003_bus_hora_llegada_bus_hora_salida'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
