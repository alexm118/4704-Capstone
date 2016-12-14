from django.shortcuts import render, get_object_or_404
from planes.models import AirbusPlane, Plane, Manufacturer, GulfstreamPlane, BoeingPlane, BlueBookPlane, Helicopter, BlueBookHelicopter
from planes.serializers import AirbusPlaneSerializer, BoeingPlaneSerializer, BluebookPlaneSerializer
from django.http import JsonResponse
from planes.forms import PlaneForm, HeliForm
from django.template.loader import render_to_string
from django.http.response import JsonResponse
from django.db.models import Q
from planes.serializers import AirbusPlaneSerializer, BoeingPlaneSerializer, CessnaPlaneSerializer
from planes.models import AirbusPlane, Plane, Manufacturer, GulfstreamPlane, BoeingPlane, CessnaPlane
from planes.forms import PlaneForm
from planes.utils import Pager

from planes.models import AirbusPlane, Plane, Manufacturer, GulfstreamPlane, BoeingPlane, BlueBookPlane, Helicopter, BlueBookHelicopter
from planes.serializers import AirbusPlaneSerializer, BoeingPlaneSerializer, BluebookPlaneSerializer
from django.http import JsonResponse
from planes.forms import PlaneForm, HeliForm

def display_airbus_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    result_dict = []
    for field in plane._meta.get_fields():
        if field.name == 'plane_ptr':
            result_dict.append(('Manufacturer', getattr(plane, field.name)))
        elif field.name == 'id':
            pass
        else:
            result_dict.append((field.name, getattr(plane, field.name)))

    return render(request, "planes/plane.html", context={'result_dict': result_dict})


def display_gulfstream_plane(request, id):
    plane = GulfstreamPlane.objects.get(id=id)
    return render(request, "planes/gulfstream_plane.html", context={'plane': plane})


def display_boeing_plane(request, id):
    plane = BoeingPlane.objects.get(id=id)
    return render(request, "planes/boeing_plane.html", context={'plane': plane})


def display_bluebook_plane(request, id):
    plane = BlueBookPlane.objects.get(id=id)
    return render(request, "planes/bluebook_plane.html", context={'plane': plane})


def display_bluebook_heli(request, id):
    heli = BlueBookHelicopter.objects.get(id=id)

    result_dict = []
    for field in heli._meta.get_fields():
        if field.name == 'helicopter_ptr':
            result_dict.append(('Manufacturer', getattr(heli, field.name)))
        elif field.name == 'id' or field.name == 'manufacturer':
            pass
        else:
            result_dict.append((field.name, getattr(heli, field.name)))

    return render(request, "helis/bluebook_heli.html", context={'result_dict': result_dict, 'heli': heli})

def display_cessna_plane(request, id):
    plane = CessnaPlane.objects.get(id=id)
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

def list_helis(request):
    helis = Helicopter.objects.all()
    form = HeliForm()
    return render(request, "helis/heli_list.html", context={'helis': helis, 'form': form})


def airbus_rest_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    serializer = AirbusPlaneSerializer(plane)
    fields = request.GET['fields']
    fields = ''.join(fields).split()
    response = {}
    for field in fields:
        response[str(field)] = serializer.data[str(field)]
    return JsonResponse(response)


def airbus_rest_plane_all(request):
    planes = AirbusPlane.objects.all()
    results = []
    for plane in planes:
        serializer = AirbusPlaneSerializer(plane)
        results.append(serializer.data)

    return JsonResponse(results, safe=False)


def airbus_rest_fields(request):
    results = [f.name for f in AirbusPlane._meta.get_fields()]
    return JsonResponse(results, safe=False)


def boeing_rest_plane(request, id):
    plane = BoeingPlane.objects.get(id=id)
    serializer = BoeingPlaneSerializer(plane)
    return JsonResponse(serializer.data)

def bluebook_rest_plane(request, id):
    plane = BlueBookPlane.objects.get(id=id)
    serializer = BluebookPlaneSerializer(plane)
    return JsonResponse(serializer.data)


def bluebook_rest_plane_all(request):
    planes = BlueBookPlane.objects.all()
    results = []
    for plane in planes:
        serializer = BluebookPlaneSerializer(plane)
        results.append(serializer.data)

    return JsonResponse(results, safe=False)


def bluebook_rest_fields(request):
    results = [f.name for f in BlueBookPlane._meta.get_fields()]
    return JsonResponse(results, safe=False)

def bluebook_rest_heli(request, id):
    plane = BlueBookHelicopter.objects.get(id=id)
    serializer = AirbusPlaneSerializer(plane)
    fields = request.GET['fields']
    fields = ''.join(fields).split()
    response = {}
    for field in fields:
        response[str(field)] = serializer.data[str(field)]
    return JsonResponse(response)


def bluebook_rest_heli_all(request):
    planes = BlueBookHelicopter.objects.all()
    results = []
    for plane in planes:
        serializer = BlueBookHelicopterSerializer(plane)
        results.append(serializer.data)

    return JsonResponse(results, safe=False)


def bluebook_rest_heli_fields(request):
    results = [f.name for f in BlueBookHelicopter._meta.get_fields()]
    return JsonResponse(results, safe=False)


def filter_plane_list(request, id):
    if request.method == 'GET':
        if int(id) != 10000:
            manufacturer = get_object_or_404(Manufacturer, id=id)
            planes = Plane.objects.filter(manufacturer=manufacturer)

def cessna_rest_plane(request, id):
    plane = CessnaPlane.objects.get(id=id)
    serializer = CessnaPlaneSerializer(plane)
    return JsonResponse(serializer.data)


def filter_plane_list(request):
    if request.method == 'POST':
        form = PlaneForm(request.POST)
        query = Q()
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']

            if model:
                query |= Q(model__icontains=model)

            if manufacturer:
                query |= Q(manufacturer__name__icontains=manufacturer)

            planes = Plane.objects.filter(query)
            pager = Pager()
            pager.page_size = 25
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
            print(form.errors)

    else:
        print('Invalid access')

    planes = Plane.objects.all().order_by('manufacturer', 'model')
    return render(request, "planes/plane_list.html", context={'planes': planes})


def filter_heli_list(request, id):
    if request.method == 'GET':
        if int(id) != 10000:
            manufacturer = get_object_or_404(Manufacturer, id=id)
            helis = Helicopter.objects.filter(manufacturer=manufacturer)
        else:
            helis = Helicopter.objects.all()
        return render(request, 'helis/panels/heli_table.html', context={'helis': helis})
    else:
        print('Invalid access')

    helis = Helicopter.objects.all().order_by('manufacturer', 'model')
    return render(request, "helis/heli_list.html", context={'helis': helis})