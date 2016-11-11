from django.contrib import admin
from planes.models import AirbusPlane, Engine, GulfstreamPlane, BoeingPlane, BlueBookPlane


admin.site.register(AirbusPlane)
admin.site.register(BlueBookPlane)
admin.site.register(BoeingPlane)
admin.site.register(Engine)
admin.site.register(GulfstreamPlane)