from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import urllib
from planes.models import BlueBookPlane, Engine


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = ["http://www.aircraftbluebook.com/Tools/ABB/ShowSpecifications.do"]

        for url in urls:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            rows = soup.find("tbody").find_all("tr")

            for row in rows:
                if "header" in row['class']:
                    manufacturer = row.find_next("td").get_text()
                    # print "NEW MANUF: ", manufacturer
                    # print ""
                else:
                    current_data = row.find_all("td")
                    model = current_data[0].get_text()
                    engine = current_data[1].get_text()
                    thrust = current_data[2].get_text()
                    max_speed_knots = current_data[3].get_text()
                    recommended_cruise_knots = current_data[4].get_text()
                    stall_knots_dirty = current_data[5].get_text()
                    fuel_gal_lbs = current_data[6].get_text()
                    all_eng_service_ceiling = current_data[7].get_text()
                    eng_out_service_ceiling = current_data[8].get_text()
                    all_eng_climb_rate = current_data[9].get_text()
                    eng_out_climb_rate = current_data[10].get_text()
                    takeoff_over_50_ft = current_data[11].get_text()
                    takeoff_ground_run = current_data[12].get_text()
                    landing_over_50_ft = current_data[13].get_text()
                    landing_ground_roll = current_data[14].get_text()
                    gross_weight_lbs = current_data[15].get_text()
                    empty_weight_lbs = current_data[16].get_text()
                    overall_length = current_data[17].get_text()
                    overall_height = current_data[18].get_text()
                    wingspan = current_data[19].get_text()
                    plane_range = current_data[20].get_text()

                    engine_model = Engine(name=engine)
                    engine_model.save()

                    if BlueBookPlane.objects.filter(model=model, manufacturer=manufacturer).exists():
                        plane = BlueBookPlane.objects.filter(model=model).first()
                        print plane.model

                    else:
                        plane = BlueBookPlane(model=model, engine=engine, thrust=thrust, max_speed_knots=max_speed_knots, recommended_cruise_knots=recommended_cruise_knots,
                                              stall_knots_dirty=stall_knots_dirty, fuel_gal_lbs=fuel_gal_lbs, all_eng_service_ceiling=all_eng_service_ceiling,
                                              eng_out_service_ceiling=eng_out_service_ceiling, all_eng_climb_rate=all_eng_climb_rate, eng_out_climb_rate=eng_out_climb_rate,
                                              takeoff_over_50_ft=takeoff_over_50_ft, takeoff_ground_run=takeoff_ground_run, landing_over_50_ft=landing_over_50_ft,landing_ground_roll=landing_ground_roll,
                                              gross_weight_lbs=gross_weight_lbs, empty_weight_lbs=empty_weight_lbs, overall_length=overall_length, overall_height=overall_height,
                                              wingspan=wingspan, plane_range=plane_range)
                        plane.save()
                        # plane.engines.add(engine)
                        plane.save()
                        print plane.model

                    print ""
                    print "Manu", manufacturer
                    print "model", model
                    print "RANDGE", plane_range
