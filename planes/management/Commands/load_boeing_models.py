from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
from planes.models import BoeingPlane


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = [
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-747-8/17",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-747-400/18",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-747-400ER/19",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-777-200ER/20",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-777-200LR/21",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-777-300/22",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-777-300ER/23",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-737-600/24",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-787-10X/25",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-737-Convertible/26",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-737-700/27",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-737-800/28",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-737-900ER/29",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-787-3/30",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-787-Dreamliner/31",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-787-9/32",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-767-200/33",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-767-300/34",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-767-400/35",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-747-8-Cargo/2",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-747-400F/3",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-Dreamlifter/4",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-767-Freighter/5",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-777-Freighter/6",
            "https://www.aircraftcompare.com/helicopter-airplane/New-Air-Force-One/36",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-BBJ/37",
            "https://www.aircraftcompare.com/helicopter-airplane/BBJ2/38",
            "https://www.aircraftcompare.com/helicopter-airplane/BBJ3/39",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-747-8-VIP/40",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-777-VIP/41",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-787-VIP/42",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-Business-Jet/43",
            "https://www.aircraftcompare.com/helicopter-airplane/C-17-Globemaster/7",
            "https://www.aircraftcompare.com/helicopter-airplane/A-10-Warthog/8",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-YAL-1/9",
            "https://www.aircraftcompare.com/helicopter-airplane/Boeing-E-6-Tacamo/10",
            "https://www.aircraftcompare.com/helicopter-airplane/EA-18G-Growler/11",
            "https://www.aircraftcompare.com/helicopter-airplane/F-15E-Strike-Eagle/12",
            "https://www.aircraftcompare.com/helicopter-airplane/F15-Silent-Eagle/13",
            "https://www.aircraftcompare.com/helicopter-airplane/F-18-Hornet/14",
            "https://www.aircraftcompare.com/helicopter-airplane/F-18-Super-Hornet/15",
            "https://www.aircraftcompare.com/helicopter-airplane/T45-Goshawk/16"]

        for url in urls:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            #range = soup(text="Travel Range")[0].find_next("div", class_="col-xs-12 col-md-12 reset").get_text()
            #range = soup(text="Range")[0].find_next("span", class_="metric").get_text()
            engine = soup(text="Engine")[0].find_next().get_text()
            seating = soup.find("div", class_="col-md-3 nopadding", id="mydiv").get_text()
            model = url.split("/")[-1]
            length = soup.find(text="Cabin Length").find_next().get_text()
            height = soup.find(text="Cabin Height").find_next().get_text()
            wingspan = soup.find(text="Wingspan").find_next().get_text()
            manufacturer = "Boeing"
            maximum_payload = soup.find(text="Maximum Payload").find_next().get_text
            baggage_volume = soup.find(text="Baggage Volume").find_next().get_text


            if BoeingPlane.objects.filter(model=model).exists():
                plane = BoeingPlane.objects.filter(model=model).first()
                print plane.model

            else:
                plane = BoeingPlane(model=model, plane_range=range, seating=seating, overall_length=length,
                                    overall_height=height, wingspan=wingspan, manufacturer=manufacturer,
                                    bulk_hold_volume=baggage_volume, total_volume=maximum_payload)
                plane.save()
                print(engine)
                plane.engines.add(engine)
                plane.save()
                print plane.model