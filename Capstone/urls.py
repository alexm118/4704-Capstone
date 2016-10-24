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
from planes.views import display_plane, list_planes, airbus_rest_plane, filter_plane_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^planes/(?P<id>[0-9]+)/$', display_plane, name="display_planes"),
    url(r'^planes/$',list_planes, name="plane_list"),
    url(r'^rest/airbus/(?P<id>[0-9]+)/$', airbus_rest_plane, name="airbus_rest_plane"),
    url(r'^planes/filter/manufacturer/$', filter_plane_list, name="filter_planes"),
]
