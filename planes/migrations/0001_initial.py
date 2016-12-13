# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-09 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='AirbusPlane',
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
        migrations.CreateModel(
            name='BlueBookPlane',
            fields=[
                ('plane_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='planes.Plane')),
                ('thrust', models.CharField(max_length=25)),
                ('max_speed_knots', models.CharField(max_length=25)),
                ('recommended_cruise_knots', models.CharField(max_length=25)),
                ('stall_knots_dirty', models.CharField(max_length=25)),
                ('fuel_gal_lbs', models.CharField(max_length=25)),
                ('all_eng_service_ceiling', models.CharField(max_length=25)),
                ('eng_out_service_ceiling', models.CharField(max_length=25)),
                ('all_eng_climb_rate', models.CharField(max_length=25)),
                ('eng_out_climb_rate', models.CharField(max_length=25)),
                ('takeoff_over_50_ft', models.CharField(max_length=25)),
                ('takeoff_ground_run', models.CharField(max_length=25)),
                ('landing_over_50_ft', models.CharField(max_length=25)),
                ('landing_ground_roll', models.CharField(max_length=25)),
                ('gross_weight_lbs', models.CharField(max_length=25)),
                ('empty_weight_lbs', models.CharField(max_length=25)),
                ('overall_length', models.CharField(max_length=25)),
                ('overall_height', models.CharField(max_length=25)),
                ('wingspan', models.CharField(max_length=25)),
                ('plane_range', models.CharField(max_length=25)),
            ],
            bases=('planes.plane',),
        ),
        migrations.CreateModel(
            name='BoeingPlane',
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
        migrations.AddField(
            model_name='plane',
            name='engines',
            field=models.ManyToManyField(related_name='engines', to='planes.Engine'),
        ),
        migrations.AddField(
            model_name='plane',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planes.Manufacturer'),
        ),
    ]
