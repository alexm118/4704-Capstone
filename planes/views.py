from django.shortcuts import render
from planes.models import AirbusPlane, Plane
from planes.serializers import AirbusPlaneSerializer
from django.http import JsonResponse


def display_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    return render(request, "planes/airbus_plane.html", context={'plane': plane})


def list_planes(request):
    planes = Plane.objects.all()
    return render(request, "planes/plane_list.html", context={'planes': planes})


def airbus_rest_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    serializer = AirbusPlaneSerializer(plane)
    return JsonResponse(serializer.data)
