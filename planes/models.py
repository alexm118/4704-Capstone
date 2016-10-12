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

