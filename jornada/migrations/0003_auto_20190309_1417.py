# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-09 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornada', '0002_auto_20190308_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornadaclass',
            name='tipo',
            field=models.CharField(choices=[('COM', 'Jornada Completa'), ('PAR', 'Jornada Parcial'), ('180', '180 horas mensuales'), ('45H', '45 horas semanales'), ('60H', '60 horas semanales'), ('ADT', 'Autorizada por la Dirección del Trabajo'), ('JBI', 'Bisemanal'), ('JRA', 'Registro de Asistencia')], default=('COM', 'Jornada Completa'), max_length=3),
        ),
    ]
