from django.contrib import admin
from planes.models import AirbusPlane, Engine, GulfstreamPlane, BoeingPlane


admin.site.register(AirbusPlane)
admin.site.register(GulfstreamPlane)
admin.site.register(Engine)