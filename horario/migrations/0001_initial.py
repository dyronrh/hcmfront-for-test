# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_inicio', models.CharField(choices=[('Lu', 'LUNES'), ('Ma', 'MARTES'), ('Mi', 'MIERCOLES'), ('Ju', 'JUEVES'), ('Vi', 'VIERNES'), ('Sa', 'SABADO'), ('Do', 'DOMINGO')], max_length=2)),
                ('dia_fin', models.CharField(blank=True, choices=[('Lu', 'LUNES'), ('Ma', 'MARTES'), ('Mi', 'MIERCOLES'), ('Ju', 'JUEVES'), ('Vi', 'VIERNES'), ('Sa', 'SABADO'), ('Do', 'DOMINGO')], max_length=2, null=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
    ]
