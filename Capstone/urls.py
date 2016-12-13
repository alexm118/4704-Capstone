"""Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from planes.views import *

all_bluebook_planes = '(aeronca|aerostar-aircraft-corporation|ag-cat-corp|aircoupe-alon|aircraft-manufacturing-design-llc|air-tractor-inc|american-champion-aircraft-corporation|american-general-aircraft|aviat-aircraft-inc|ayres-corp|b-bar-d-aviation-inc|beechcraft-hawker-beechcraft|bellanca-inc|bombardier-aerospace-business-aircraft|cessna-aircraft-company|cirrus-design-corporation|columbia-aircraft-mfg|commander-premier-aircraft|cubcrafters-inc|dassault-falcon-jet|de-havilland-see-also-bombardier|diamond-aircraft|eads-socata-aircraft|eagle|eclipse-aviation|embraer-aircraft-empresa-brasileira|eurofox-rollison-lsa-inc|excalibur-aviation|fairchild-m7-aerospace|flight-design-usa|gobosh-aviation|gulfstream-aerospace|hawker-beechcraft|iai|jabiru-usa-sport-aircraft-llc|lake-aircraft|liberty-aerospace-inc|lockheed-martin-aircraft|luscombe-aircraft-quartz-mountain-aero|machen-inc|maule-air-inc|melex-usa-inc|mitsubishi-diamond|mooney-aircraft|navion-aircraft-international|piaggio-america|pilatus-business-aircraft|piper-aircraft|ram-aircraft-lp|remos-aircraft-inc|riley-super-skyrocket|rocket-engineering-jetprop-llc|rockwell-meyers-200|sabreliner-corp|sierra-industries|sportair-usa-lc|stinson|swift|symphony-aircraft-industries|taylorcraft-inc|tecnam-aircraft|tradewind-turbines|twin-commander-ac|varga)'
all_bluebook_helis = '(agusta-aerospace-corporation|bell-helicopter-a-textron-company|enstrom-helicopter-corporation-usa|eurocopter|hiller-aircraft-corp|md-helicopters-incorporated|robinson-helicopter|schweizer-aircraft|sikorsky-aircraft)'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^planes/airbus/(?P<id>[0-9]+)/$', display_airbus_plane, name="display_airbus_plane"),
    url(r'^planes/gulfstream/(?P<id>[0-9]+)/$', display_gulfstream_plane, name="display_gulfstream_plane"),
    url(r'^planes/boeing/(?P<id>[0-9]+)/$', display_boeing_plane, name="display_boeing_plane"),
    url(r'^planes/bluebook/(?P<id>[0-9]+)/$', display_bluebook_plane, name="display_bluebook_plane"),

    url(r'^planes/' + all_bluebook_planes + '/(?P<id>[0-9]+)/$',
        display_bluebook_plane, name="display_bluebook_plane"),

    url(r'^helis/' + all_bluebook_helis + '/(?P<id>[0-9]+)/$',
        display_bluebook_heli, name="display_bluebook_heli"),

    url(r'^rest/' + all_bluebook_planes + '/$', bluebook_rest_plane_all, name='rest_bluebook_all'),
    url(r'^rest/' + all_bluebook_planes + '/fields/$', bluebook_rest_fields, name='bluebook_fields'),
    url(r'^rest/' + all_bluebook_planes + '/(?P<id>[0-9]+)/$', bluebook_rest_plane, name="bluebook_rest_plane"),

    url(r'^rest/' + all_bluebook_helis + '/$', bluebook_rest_heli_all, name='rest_bluebook_heli_all'),
    url(r'^rest/' + all_bluebook_helis + '/fields/$', bluebook_rest_heli_fields, name='bluebook_heli_fields'),
    url(r'^rest/' + all_bluebook_helis + '/(?P<id>[0-9]+)/$', bluebook_rest_heli, name="bluebook_rest_heli"),

    url(r'^planes/$', list_planes, name="plane_list"),
    url(r'^helis/$',list_helis, name="plane_list"),
    url(r'^planes/filter/manufacturer/(?P<id>[0-9]+)/$', filter_plane_list, name="filter_planes"),
    url(r'^helis/filter/manufacturer/(?P<id>[0-9]+)/$', filter_heli_list, name="filter_helis"),

    url(r'^planes/cessna/(?P<id>[0-9]+)/$', display_cessna_plane, name="display_cessna_plane"),
    url(r'^planes/$',list_planes, name="plane_list"),
    url(r'^rest/airbus/$', airbus_rest_plane_all, name='rest_airbus_all'),
    url(r'^rest/airbus/fields/$', airbus_rest_fields, name='airbus_fields'),
    url(r'^rest/airbus/(?P<id>[0-9]+)/$', airbus_rest_plane, name="airbus_rest_plane"),
    url(r'^planes/filter/$', filter_plane_list, name="filter_planes"),

]
