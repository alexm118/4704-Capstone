from django.contrib import admin
from planes.models import AirbusPlane, Engine, GulfstreamPlane, BoeingPlane, CessnaPlane


admin.site.register(AirbusPlane)
admin.site.register(GulfstreamPlane)
admin.site.register(BoeingPlane)
admin.site.register(CessnaPlane)
admin.site.register(Engine)