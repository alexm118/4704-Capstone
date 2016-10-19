from __future__ import unicode_literals

from django.db import models


class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Plane(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, models.SET_NULL, null=True, blank=False)
    model = models.CharField(max_length=25)
    engines = models.ManyToManyField(Engine, related_name='engines')

    def get_unique_manufacturers(self):
        planes = Plane.objects.all()
        manufacturer_list = []
        for plane in planes:
            tuple = (plane.manufacturer, plane.manufacturer)
            if tuple not in manufacturer_list:
                manufacturer_list.append(tuple)
        print(manufacturer_list)
        return manufacturer_list

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

