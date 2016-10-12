from django.shortcuts import render
from planes.models import AirbusPlane


# Create your views here.
def display_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    return render(request, "planes/airbus_plane.html", context={'plane': plane})


def list_planes(request):
    planes = AirbusPlane.objects.all()
    return render(request, "planes/plane_list.html", context={'planes': planes})