from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
import re
from planes.models import BoeingPlane, Manufacturer, Engine


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = [
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-747-8/17",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-747-400/18",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-747-400ER/19",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-777-200ER/20",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-777-200LR/21",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-777-300/22",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-777-300ER/23",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-737-600/24",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-787-10X/25",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-737-Convertible/26",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-737-700/27",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-737-800/28",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-737-900ER/29",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-787-3/30",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-787-Dreamliner/31",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-787-9/32",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-767-200/33",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-767-300/34",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-767-400/35",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-747-8-Cargo/2",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-747-400F/3",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-Dreamlifter/4",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-767-Freighter/5",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-777-Freighter/6",
            "http://www.aircraftcompare.com/helicopter-airplane/New-Air-Force-One/36",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-BBJ/37",
            "http://www.aircraftcompare.com/helicopter-airplane/BBJ2/38",
            "http://www.aircraftcompare.com/helicopter-airplane/BBJ3/39",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-747-8-VIP/40",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-777-VIP/41",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-787-VIP/42",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-Business-Jet/43",
            "http://www.aircraftcompare.com/helicopter-airplane/C-17-Globemaster/7",
            "http://www.aircraftcompare.com/helicopter-airplane/A-10-Warthog/8",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-YAL-1/9",
            "http://www.aircraftcompare.com/helicopter-airplane/Boeing-E-6-Tacamo/10",
            "http://www.aircraftcompare.com/helicopter-airplane/EA-18G-Growler/11",
            "http://www.aircraftcompare.com/helicopter-airplane/F-15E-Strike-Eagle/12",
            "http://www.aircraftcompare.com/helicopter-airplane/F15-Silent-Eagle/13",
            "http://www.aircraftcompare.com/helicopter-airplane/F-18-Hornet/14",
            "http://www.aircraftcompare.com/helicopter-airplane/F-18-Super-Hornet/15",
            "http://www.aircraftcompare.com/helicopter-airplane/T45-Goshawk/16"]

        for url in urls:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            range = soup(text="Travel Range -")[0].find_next("div").get_text()
            engine = soup.find(text = re.compile("Engine")).replace("Engine - ",'')
            seating = soup.find("div", class_="col-md-3 nopadding", id="mydiv").get_text()
            model = url.split("/")[-2].replace("Boeing-",'')
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

            if BoeingPlane.objects.filter(model=model).exists():
                plane = BoeingPlane.objects.filter(model=model).first()
                plane.engines.add(*engine_list)
                print(plane.engines.all())
                plane.save()
                print plane.model

            else:
                plane = BoeingPlane(model=model, plane_range=range, seating=seating, overall_length=length,
                                    overall_height=height, wingspan=wingspan, manufacturer=manufacturer,
                                    bulk_hold_volume=baggage_volume, total_volume=maximum_payload)
                plane.save()
                plane.engines.add(*engine_list)
                plane.save()
                print plane.model