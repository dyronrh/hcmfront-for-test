# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JornadaClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('jc', 'Jornada Completa'), ('jp', 'Jornada Parcial'), ('j180h', '180 horas mensuales'), ('j45h', '45 horas semanales'), ('j60h', '60 horas semanales'), ('jadt', 'Autorizada por la Dirección del Trabajo'), ('jb', 'Bisemanal'), ('jra', 'Registro de Asistencia')], max_length=6)),
            ],
        ),
    ]
