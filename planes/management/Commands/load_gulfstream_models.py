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
            range = soup(text="Maximum Range *")[0].find_next("td").get_text()
            model = url.split("-")[-1].upper()
            seating = soup(text="Passengers")[1].find_next("td").get_text()
            length = soup(text="Length")[1].find_next("td").get_text()
            height = soup(text="Height")[1].find_next("td").get_text()
            wingspan = soup(text="Overall Span")[1].find_next("td").get_text() 
            manufacturer = "Gulfstream"
            if Manufacturer.objects.filter(name=manufacturer).exists():
                manufacturer = Manufacturer.objects.filter(name=manufacturer).first()
            else:
                manufacturer = Manufacturer(name=manufacturer)
                manufacturer.save()

            if GulfstreamPlane.objects.filter(model=model).exists():
                    plane = GulfstreamPlane.objects.filter(model=model).first()
                    print plane.model

            else:
                plane = GulfstreamPlane(model=model, plane_range=range, seating=seating, overall_length=length,
                                    overall_height=height, wingspan=wingspan, manufacturer=manufacturer)
                plane.save()
                print plane.model