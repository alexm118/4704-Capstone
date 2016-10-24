from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
from planes.models import AirbusPlane, Engine, Manufacturer


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = ["http://www.airbus.com/aircraftfamilies/passengeraircraft/a320family/a318/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a320family/a319/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a320family/a320/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a320family/a321/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a330family/a330-200/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a330family/a330-300/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a340family/a340-300/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a340family/a340-500/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a340family/a340-600/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a350xwbfamily/a350-800/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a350xwbfamily/a350-900/specifications/",
                "http://www.airbus.com/aircraftfamilies/passengeraircraft/a350xwbfamily/a350-1000/specifications/"]
        for url in urls:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            range = soup(text="Range")[0].find_next("span", class_="metric").get_text()
            seating = soup.find("div", class_="max-pax").contents[-2].get_text()
            model = url.split("/")[-3]
            length = soup.find("div", class_="overall-length").find_next("span", class_="metric").get_text()
            height = soup.find("div", class_="height").find_next("span", class_="metric").get_text()
            wingspan = soup.find("div", class_="wing-span").find_next("span", class_="metric").get_text()
            manufacturer = "Airbus"
            bulk_hold_volume = soup(text="Bulk hold volume")[0].find_next("span", class_="metric").get_text()
            total_volume = soup(text="Total volume (Bulk loading)")[0].find_next("span", class_="metric").get_text()
            engine_list = []
            engine_name_elements = soup.find("div", {"id": "box-engines"}).find_all("th")
            for element in engine_name_elements:
                if element.find("i"):
                    engine_list.append(str(element.find("i").get_text()))

            engines = []

            if Manufacturer.objects.filter(name=manufacturer):
                manufacturer = Manufacturer.objects.filter(name=manufacturer).first()
            else:
                manufacturer = Manufacturer(name=manufacturer)
                manufacturer.save()

            for engine in engine_list:
                if Engine.objects.filter(name=engine).exists():
                    engine_model = Engine.objects.filter(name=engine).first()
                    engines.append(engine_model)
                else:
                    engine_model = Engine(name=engine)
                    engine_model.save()
                    engines.append(engine_model)

            if AirbusPlane.objects.filter(model=model).exists():
                plane = AirbusPlane.objects.filter(model=model).first()
                print plane.model

            else:
                plane = AirbusPlane(model=model, plane_range=range, seating=seating, overall_length=length,
                                    overall_height=height, wingspan=wingspan, manufacturer=manufacturer,
                                    bulk_hold_volume=bulk_hold_volume, total_volume=total_volume)
                plane.save()
                print(engines)
                plane.engines.add(*engines)
                plane.save()
                print plane.model
