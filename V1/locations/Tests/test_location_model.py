from django.test import TestCase
from V1.locations.models import Location
from V1.devices.models import Device
from V1.users.models import User
import time

# python manage.py test V1/locations/tests
from IPython import embed

class LocationModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        device = Device.objects.create(user=user,
                                       sms_number='7192710056',
                                       pin_lat=39.996665,
                                       pin_long=-105.234931)

        input_location = Location.objects.create(device=device, lat=39.996665, long=-105.234931)

        saved_location = Location.objects.first()
        count = Location.objects.count()

        self.assertEqual(saved_location.lat, 39.996665)
        self.assertEqual(saved_location.long, -105.234931)
        self.assertEqual(saved_location.device.id, device.id)
        self.assertEqual(count, 1)


    def test_device_calculates_distance_for_same_cords(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        device = Device.objects.create(user=user,
                                       sms_number='7192710056',
                                       pin_lat=39.996665,
                                       pin_long=-105.234931)

        input_location = Location.objects.create(device=device, lat=39.996665, long=-105.234931)

        saved_location = Location.objects.first()

        self.assertEqual(saved_location.lat, 39.996665)
        self.assertEqual(saved_location.long, -105.234931)
        self.assertEqual(saved_location.distance, 0)


    def test_device_calculates_distance_for_dif_cords(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        device = Device.objects.create(user=user,
                                       sms_number='7192710056',
                                       pin_lat=39.996665,
                                       pin_long=-105.234931)

        input_location = Location.objects.create(device=device, lat=39.985555, long=-105.235555)

        saved_location = Location.objects.first()

        self.assertEqual(saved_location.lat, 39.985555)
        self.assertEqual(saved_location.long, -105.235555)
        self.assertEqual(saved_location.distance, 1234.74348675545)

    def test_ordering_of_locations(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        device = Device.objects.create(user=user,
                                       sms_number='7192710056',
                                       pin_lat=39.996665,
                                       pin_long=-105.234931)

        location_1 = Location.objects.create(device=device, lat=38.985555, long=-105.235555)
        time.sleep(1)
        location_2 = Location.objects.create(device=device, lat=37.985555, long=-105.235555)
        time.sleep(1)
        location_3 = Location.objects.create(device=device, lat=36.985555, long=-105.235555)
        time.sleep(1)
        location_4 = Location.objects.create(device=device, lat=35.985555, long=-105.235555)
        time.sleep(1)
        location_5 = Location.objects.create(device=device, lat=34.985555, long=-105.235555)

        locations = Location.objects.all()
        self.assertEqual(locations[0], location_5)
        self.assertEqual(locations[1], location_4)
        self.assertEqual(locations[2], location_3)
        self.assertEqual(locations[3], location_2)
        self.assertEqual(locations[4], location_1)
