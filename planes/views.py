from django.shortcuts import render
from planes.models import AirbusPlane, Plane, Manufacturer
from planes.serializers import AirbusPlaneSerializer
from django.http import JsonResponse
from planes.forms import PlaneForm


def display_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    return render(request, "planes/airbus_plane.html", context={'plane': plane})


def list_planes(request):
    planes = Plane.objects.all()
    form = PlaneForm()
    return render(request, "planes/plane_list.html", context={'planes': planes, 'form': form})


def airbus_rest_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    serializer = AirbusPlaneSerializer(plane)
    return JsonResponse(serializer.data)


def filter_plane_list(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(id=manufacturer_id)
    planes = Plane.objects.filter(manufacturer=manufacturer)
    return render(request, 'planes/tables/plane_table.html', context={'planes': planes})
