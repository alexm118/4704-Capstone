from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
from planes.models import GulfstreamPlane, Engine, Manufacturer


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = ["http://www.gulfstream.com/aircraft/gulfstream-g650er",
                "http://www.gulfstream.com/aircraft/gulfstream-g650",
                "http://www.gulfstream.com/aircraft/gulfstream-g600",
                "http://www.gulfstream.com/aircraft/gulfstream-g550",
                "http://www.gulfstream.com/aircraft/gulfstream-g500",
                "http://www.gulfstream.com/aircraft/gulfstream-g450",
                "http://www.gulfstream.com/aircraft/gulfstream-g280"]
        for url in urls:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            range = soup(text="Maximum Range *")[1].find_next("td").get_text()
            model = url.split("-")[-1].upper()
            seating = soup(text="Passengers")[1].find_next("td").get_text()
            length = soup(text="Length")[1].find_next("td").get_text()
            height = soup(text="Height")[1].find_next("td").get_text()
            wingspan = soup(text="Overall Span")[1].find_next("td").get_text() 
            baggage_volume = soup(text="Baggage Compartment")[1].find_next("td").get_text()
            cabin_volume = soup(text="Cabin Volume")[1].find_next("td").get_text()
            total_volume = str(float(baggage_volume.split()[0]) + float(cabin_volume.split()[0])) + ' cu m'
            engine = soup(text="Engines")[1].find_next("td").get_text()
            manufacturer = "Gulfstream"
            print engine
            engines = []

            if Manufacturer.objects.filter(name=manufacturer).exists():
                manufacturer = Manufacturer.objects.filter(name=manufacturer).first()
            else:
                manufacturer = Manufacturer(name=manufacturer)
                manufacturer.save()
            
            if Engine.objects.filter(name=engine).exists():
                engine_model = Engine.objects.filter(name=engine).first()
                engines.append(engine_model)
            else:
                engine_model = Engine(name=engine)
                engine_model.save()
                engines.append(engine_model)
            
            if GulfstreamPlane.objects.filter(model=model).exists():
                    plane = GulfstreamPlane.objects.filter(model=model).first()
                    print plane.model

            else:
                plane = GulfstreamPlane(model=model, plane_range=range, seating=seating, overall_length=length,
                                    overall_height=height, wingspan=wingspan, manufacturer=manufacturer,
                                    bulk_hold_volume=baggage_volume, total_volume=total_volume)
                plane.save()
                print(engines)
                plane.engines.add(*engines)
                plane.save()
                print plane.model