import os
# Configure settings for project
# Need to run this before calling models from application
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SAFETTY.settings')

import django
# import settings
django.setup()

from validate_car.models import Car,Driver

import random
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

routes = ['from/around Port of Spain westward to the Valley','from POS to Sandre Grande','from POS to San Fernando (including Chaguanas, Couva, Gasparillo)','from San Fernando to Princes Town','from San Fernando into Southwest (Erin, Penal, Point Fortin,Siparia)','around the island of Tobago']

def populate_cars(N=5):

    for _ in range(N):
        fake_make_model_year = fake.vehicle_year_make_model()
        fake_license_plate = fake.bothify(text='HD? ####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        fake_colour = fake.safe_color_name().capitalize()
        fake_route = random.choice(routes)

        car = Car.objects.get_or_create(make_model_year=fake_make_model_year,license_plate=fake_license_plate,colour=fake_colour,route=fake_route)[0]
        car.save()

def populate_drivers(N=5):

    for _ in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_dob = fake.bothify(text='19##')
        fake_permit_number = fake.bothify(text='9#####')
        fake_address = fake.street_address() + ', ' + fake.city()
        fake_contact_number = fake.bothify(text='(868)2##-####')

        driver = Driver.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,dob=fake_dob,permit_number=fake_permit_number,address=fake_address,contact_number=fake_contact_number)[0]
        driver.save()

if __name__ == '__main__':
    print("POPULATING")
    populate_cars(20)
    populate_drivers(20)
    print("COMPLETE")
