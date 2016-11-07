from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
import re
from planes.models import CessnaPlane, Manufacturer, Engine


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = [
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Super-Cargomaster/127",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Super-Cargomaster-EX/503",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Hemisphere/496",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Longitude/498",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Columbus/129",
            "https://www.aircraftcompare.com/helicopter-airplane/Citation-Sovereign/130",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-X/131",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Latitude/497",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Sovereign-Plus/500",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-X-Plus/501",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-CJ3/132",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation/133",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-CJ2/134",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-CJ4/135",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Encore/136",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-XLS/137",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Grand-Caravan/128",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Grand-Caravan-EX/502",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-M2/499",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Citation-Mustang/148",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Caravan-Amphibian/126",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-162-Skycatcher/141",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-350/138",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-400/139",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Caravan/140",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-172-Skyhawk/142",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-172-SP/143",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-182/144",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-182-Turbo-Skylane/145",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-206/146",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-Turbo-Stationair/147",
            "https://www.aircraftcompare.com/helicopter-airplane/Cessna-TTx/504"]

        for url in urls:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            range = soup(text="Travel Range -")[0].find_next("div").get_text()
            engine = soup.find(text = re.compile("Engine")).replace("Engine - ",'')
            seating = soup.find("div", class_="col-md-3 nopadding", id="mydiv").get_text()
            model = url.split("/")[-2].replace("Boeing ",'')
            lengthF = soup.find(text= re.compile("Cabin Length")).split(' ')
            length = lengthF[-3]
            heightF = soup.find(text=re.compile("Cabin Height")).split(' ')
            height = heightF[-3]
            wingspanF = soup.find(text=re.compile("Wingspan")).split(' ')
            wingspan = wingspanF[-3]
            manufacturer = "Boeing"
            maximum_payloadF = soup.find(text=re.compile("Maximum Payload")).split(' ')
            maximum_payload = maximum_payloadF[-3]
            baggage_volumeF = soup.find(text=re.compile("Baggage Volume")).replace(u'\xa0',' ').split(' ')
            baggage_volume = baggage_volumeF[-3]

            if Manufacturer.objects.filter(name=manufacturer).exists():
                manufacturer = Manufacturer.objects.filter(name=manufacturer).first()
            else:
                manufacturer = Manufacturer(name=manufacturer)
                manufacturer.save()

            engine_list = []
            if Engine.objects.filter(name=engine).exists():
                engine = Engine.objects.filter(name=engine).first()
                engine_list.append(engine)
            else:
                engine = Engine(name=engine)
                engine.save()
                engine_list.append(engine)

            if CessnaPlane.objects.filter(model=model).exists():
                plane = CessnaPlane.objects.filter(model=model).first()
                plane.engines.add(*engine_list)
                print(plane.engines.all())
                plane.save()
                print plane.model

            else:
                plane = CessnaPlane(model=model, plane_range=range, seating=seating, overall_length=length,
                                    overall_height=height, wingspan=wingspan, manufacturer=manufacturer,
                                    bulk_hold_volume=baggage_volume, total_volume=maximum_payload)
                plane.save()
                plane.engines.add(*engine_list)
                plane.save()
                print plane.model