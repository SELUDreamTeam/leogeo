# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 14:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('area', models.IntegerField(blank=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('depth', models.FloatField(blank=True)),
                ('waveheight', models.FloatField(blank=True)),
                ('velocity', models.FloatField(blank=True)),
                ('wind_velocity', models.FloatField(blank=True, verbose_name='Wind Speed')),
                ('trib_width', models.FloatField(blank=True, verbose_name='Tributary Width')),
                ('trib_count', models.FloatField(blank=True, verbose_name='Tributary Count')),
                ('fetch', models.FloatField(blank=True)),
                ('ufarea', models.FloatField(blank=True, verbose_name='Up Flow Area')),
                ('tide_range', models.FloatField(blank=True, verbose_name='Tide Range')),
                ('turbidity', models.FloatField(blank=True)),
                ('score', models.FloatField(blank=True)),
            ],
        ),
    ]
