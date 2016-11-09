from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http.response import JsonResponse
from planes.models import AirbusPlane, Plane, Manufacturer, GulfstreamPlane, BoeingPlane
from planes.serializers import AirbusPlaneSerializer, BoeingPlaneSerializer
from django.http import JsonResponse
from planes.forms import PlaneForm
from planes.utils import Pager


def display_airbus_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    return render(request, "planes/airbus_plane.html", context={'plane': plane})


def display_gulfstream_plane(request, id):
    plane = GulfstreamPlane.objects.get(id=id)
    return render(request, "planes/gulfstream_plane.html", context={'plane': plane})


def display_boeing_plane(request, id):
    plane = BoeingPlane.objects.get(id=id)
    return render(request, "planes/boeing_plane.html", context={'plane': plane})


def list_planes(request):
    if request.method == "POST":
        form = PlaneForm(request.POST)
        if form.is_valid():
            page = form.cleaned_data['page']
            manufacturer = form.cleaned_data['manufacturer']
            if manufacturer:
                planes = Plane.objects.filter(manufacturer=manufacturer).order_by('manufacturer', 'model')
            else:
                planes = Plane.objects.all().order_by('manufacturer', 'model')
            pager = Pager()
            pager.page_size = 25
            pager.data_set = planes
            pager.get_paged_items(page)
            context = {
                'planes': pager.paged_items,
                'pager': pager
            }
            return_data = {
                'planes': render_to_string('planes/panels/plane_table.html', context=context),
                'pager': render_to_string('planes/panels/pager.html', context=context)
            }
            return JsonResponse(return_data)
        else:
            print(form.errors)

    else:
        planes = Plane.objects.all().order_by('manufacturer', 'model')
        form = PlaneForm()
        pager = Pager()
        pager.page_size = 25
        pager.data_set = planes
        pager.get_paged_items()
        return render(request, "planes/plane_list.html", context={'planes': pager.paged_items, 'form': form, 'pager': pager})


def airbus_rest_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    serializer = AirbusPlaneSerializer(plane)
    return JsonResponse(serializer.data)


def boeing_rest_plane(request, id):
    plane = BoeingPlane.objects.get(id=id)
    serializer = BoeingPlaneSerializer(plane)
    return JsonResponse(serializer.data)


def filter_plane_list(request, id):
    if request.method == 'GET':
        manufacturer = Manufacturer.objects.filter(id=id)
        planes = Plane.objects.filter(manufacturer=manufacturer).order_by('model')
        pager = Pager()
        pager.page_size = 10
        pager.data_set = planes
        pager.get_paged_items()
        context = {
            'planes': pager.paged_items,
            'pager': pager
        }
        return_data = {
            'planes': render_to_string('planes/panels/plane_table.html', context=context),
            'pager': render_to_string('planes/panels/pager.html', context=context)
        }
        return JsonResponse(return_data)
    else:
        print('Invalid access')

    planes = Plane.objects.all().order_by('manufacturer', 'model')
    return render(request, "planes/plane_list.html", context={'planes': planes})