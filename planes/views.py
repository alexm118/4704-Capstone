from django.shortcuts import render, get_object_or_404
from planes.models import AirbusPlane, Plane, Manufacturer, GulfstreamPlane, BoeingPlane, BlueBookPlane, Helicopter, BlueBookHelicopter
from planes.serializers import AirbusPlaneSerializer, BoeingPlaneSerializer, BluebookPlaneSerializer
from django.http import JsonResponse
from planes.forms import PlaneForm, HeliForm


def display_airbus_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    return render(request, "planes/airbus_plane.html", context={'plane': plane})


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

def list_planes(request):
    planes = Plane.objects.all()
    form = PlaneForm()
    return render(request, "planes/plane_list.html", context={'planes': planes, 'form': form})

def list_helis(request):
    helis = Helicopter.objects.all()
    form = HeliForm()
    return render(request, "helis/heli_list.html", context={'helis': helis, 'form': form})


def airbus_rest_plane(request, id):
    plane = AirbusPlane.objects.get(id=id)
    serializer = AirbusPlaneSerializer(plane)
    return JsonResponse(serializer.data)

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
        else:
            planes = Plane.objects.all()
        return render(request, 'planes/panels/plane_table.html', context={'planes': planes})
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