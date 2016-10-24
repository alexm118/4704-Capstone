from django.shortcuts import render, get_object_or_404
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


def filter_plane_list(request, id):
    if request.method == 'GET':
        manufacturer = get_object_or_404(Manufacturer, id=id)
        planes = Plane.objects.filter(manufacturer=manufacturer)
        return render(request, 'planes/panels/plane_table.html', context={'planes': planes})
    else:
        print('Invalid access')

    planes = Plane.objects.all().order_by('manufacturer', 'model')
    return render(request, "planes/plane_list.html", context={'planes': planes})