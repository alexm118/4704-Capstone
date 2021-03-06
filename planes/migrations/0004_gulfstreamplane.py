# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0003_auto_20161019_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='GulfstreamPlane',
            fields=[
                ('plane_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='planes.Plane')),
                ('plane_range', models.CharField(max_length=25)),
                ('seating', models.CharField(max_length=25)),
                ('bulk_hold_volume', models.CharField(max_length=25)),
                ('wingspan', models.CharField(max_length=25)),
                ('overall_length', models.CharField(max_length=25)),
                ('overall_height', models.CharField(max_length=25)),
                ('total_volume', models.CharField(max_length=25)),
                ('thrust', models.CharField(max_length=25)),
            ],
            bases=('planes.plane',),
        ),
    ]
