from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
from planes.models import BlueBookHelicopter, Manufacturer


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "http://www.aircraftbluebook.com/Tools/ABB/ShowSpecifications.do"

        manu=0
        data = urllib.urlopen(url)
        html = data.read()

        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find("div", {"id": "helicopter"}).find("tbody").find_all("tr")

        for row in rows:
            if "header" in row['class']:
                manufacturer = row.find_next("td").get_text()

                if Manufacturer.objects.filter(name=manufacturer).exists():
                    manufacturer = Manufacturer.objects.filter(name=manufacturer).first()
                else:
                    manufacturer = Manufacturer(name=manufacturer)
                    manufacturer.save()
                    manu = manu + 1
                print "NEW MANUF: ", manufacturer

            else:
                current_data = row.find_all("td")
                model = current_data[0].get_text()
                max_speed_knots = current_data[1].get_text()
                cruise_knots = current_data[2].get_text()
                vne_knots = current_data[3].get_text()
                roc_knots = current_data[4].get_text()
                cruise_time = current_data[5].get_text()
                fueld_avg_gph = current_data[6].get_text()
                ful_std_usable_gas = current_data[7].get_text()
                fuel_opt_gal = current_data[8].get_text()
                gross_internal_load = current_data[9].get_text()
                gross_external_load = current_data[10].get_text()
                empty_weight_lbs = current_data[11].get_text()
                external_load_limit = current_data[12].get_text()
                service_ceiling_all_engs = current_data[13].get_text()
                hige_max_gross = current_data[14].get_text()
                hoge_max_gross = current_data[15].get_text()
                mr_blades_dia = current_data[16].get_text()
                num_blades = current_data[17].get_text()
                blade_material = current_data[18].get_text()
                roto_type = current_data[19].get_text()
                storage_width = current_data[20].get_text()
                overall_length = current_data[21].get_text()
                overall_height = current_data[22].get_text()


                if BlueBookHelicopter.objects.filter(model=model, manufacturer=manufacturer).exists():
                    heli = BlueBookHelicopter.objects.filter(model=model).first()
                    # print "exists: ", heli.model

                else:
                    heli = BlueBookHelicopter(model=model, manufacturer=manufacturer, max_speed_knots=max_speed_knots,cruise_knots=cruise_knots, vne_knots=vne_knots, roc_knots=roc_knots,cruise_time=cruise_time,fueld_avg_gph=fueld_avg_gph,ful_std_usable_gas=ful_std_usable_gas,fuel_opt_gal=fuel_opt_gal,gross_internal_load=gross_internal_load,gross_external_load=gross_external_load,
                                              empty_weight_lbs=empty_weight_lbs,external_load_limit=external_load_limit,service_ceiling_all_engs=service_ceiling_all_engs,hige_max_gross=hige_max_gross,hoge_max_gross=hoge_max_gross,mr_blades_dia=mr_blades_dia,num_blades=num_blades,blade_material=blade_material,roto_type=roto_type,storage_width=storage_width,
                                              overall_length=overall_length,overall_height=overall_height)
                    heli.save()
                    print "Saved: ", heli.model

                    # print ""
                    # print "Manu", manufacturer
                    # print "model", model

        print "Total manufacturers: ", manu