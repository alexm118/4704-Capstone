from __future__ import unicode_literals

from django.db import models


class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Plane(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)
    model = models.CharField(max_length=25)
    engines = models.ManyToManyField(Engine, related_name='engines')

    @staticmethod
    def get_unique_manufacturers():
        planes = Plane.objects.all()
        manufacturer_list = [(10000, 'All'),]
        for plane in planes:
            tuple = (plane.manufacturer.id, plane.manufacturer)
            if tuple not in manufacturer_list:
                manufacturer_list.append(tuple)
        return manufacturer_list

    def __unicode__(self):
        return self.manufacturer.name


class AirbusPlane(Plane):
    plane_range = models.CharField(max_length=25)
    seating = models.CharField(max_length=25)
    bulk_hold_volume = models.CharField(max_length=25)
    wingspan = models.CharField(max_length=25)
    overall_length = models.CharField(max_length=25)
    overall_height = models.CharField(max_length=25)
    total_volume = models.CharField(max_length=25)
    thrust = models.CharField(max_length=25)

    def __unicode__(self):
        return self.model


class GulfstreamPlane(Plane):
    plane_range = models.CharField(max_length=25)
    seating = models.CharField(max_length=25)
    bulk_hold_volume = models.CharField(max_length=25)
    wingspan = models.CharField(max_length=25)
    overall_length = models.CharField(max_length=25)
    overall_height = models.CharField(max_length=25)
    total_volume = models.CharField(max_length=25)
    thrust = models.CharField(max_length=25)
    #engines = models.ManyToManyField(Engine, related_name='gstream_engines')

    def __unicode__(self):
        return self.model


class BoeingPlane(Plane):
    plane_range = models.CharField(max_length=25)
    seating = models.CharField(max_length=25)
    bulk_hold_volume = models.CharField(max_length=25)
    wingspan = models.CharField(max_length=25)
    overall_length = models.CharField(max_length=25)
    overall_height = models.CharField(max_length=25)
    total_volume = models.CharField(max_length=25)
    thrust = models.CharField(max_length=25)

    def __unicode__(self):
        return self.manufacture.name


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