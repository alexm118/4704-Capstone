from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib



class Command(BaseCommand):
    def handle(self, *args, **options):
        html = urllib.urlopen("http://www.airbus.com/aircraftfamilies/passengeraircraft/a320family/a318/specifications/").read()
        soup = BeautifulSoup(html, "html.parser")
        range = soup(text="Range")[0].find_next("span", class_="metric").get_text()
        seating = soup.find("div", class_="max-pax").contents[-2].get_text()
