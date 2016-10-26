from __future__ import unicode_literals

from django.db import models


class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Plane(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=25)
    engines = models.ManyToManyField(Engine, related_name='engines')

    def __str__(self):
        return self.manufacturer


class AirbusPlane(Plane):
    plane_range = models.CharField(max_length=25)
    seating = models.CharField(max_length=25)
    bulk_hold_volume = models.CharField(max_length=25)
    wingspan = models.CharField(max_length=25)
    overall_length = models.CharField(max_length=25)
    overall_height = models.CharField(max_length=25)
    total_volume = models.CharField(max_length=25)
    thrust = models.CharField(max_length=25)

    def __str__(self):
        return self.model

class BlueBookPlane(Plane):
    thrust = models.CharField(max_length=25)
    max_speed_knots = models.CharField(max_length=25)
    recommended_cruise_knots = models.CharField(max_length=25)
    stall_knots_dirty = models.CharField(max_length=25)
    fuel_gal_lbs = models.CharField(max_length=25)
    all_eng_service_ceiling = models.CharField(max_length=25)
    eng_out_service_ceiling = models.CharField(max_length=25)
    all_eng_climb_rate = models.CharField(max_length=25)
    eng_out_climb_rate = models.CharField(max_length=25)
    takeoff_over_50_ft = models.CharField(max_length=25)
    takeoff_ground_run = models.CharField(max_length=25)
    landing_over_50_ft = models.CharField(max_length=25)
    landing_ground_roll = models.CharField(max_length=25)
    gross_weight_lbs = models.CharField(max_length=25)
    empty_weight_lbs = models.CharField(max_length=25)
    overall_length = models.CharField(max_length=25)
    overall_height = models.CharField(max_length=25)
    wingspan = models.CharField(max_length=25)
    plane_range = models.CharField(max_length=25)
    
    def __str__(self):
        return self.model

