from __future__ import unicode_literals

from django.db import models

class AirbusPlane(models.Model):
    plane_range = models.CharField(max_length=25)
    seating = models.CharField(max_length=25)
    payload = models.CharField(max_length=25)
    wingspan = models.CharField(max_length=25)
    overall_length = models.CharField(max_length=25)
    overall_height = models.CharField(max_length=25)

