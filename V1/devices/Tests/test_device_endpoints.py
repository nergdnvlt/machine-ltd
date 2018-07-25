from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from V1.devices.models import Device
from V1.users.models import User
from V1.locations.models import Location
import json

from IPython import embed

# python manage.py test V1/devices/tests


class DeviceEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.thrasher = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        self.device = Device.objects.create(user=self.thrasher,
                                            sms_number='7192710056',
                                            pin_lat=39.996292,
                                            pin_long=-105.23503)

    def test_single_device_retrieve(self):
        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['sms_number'], self.device.sms_number)
        self.assertEqual(device['pin_lat'], self.device.pin_lat)
        self.assertEqual(device['pin_long'], self.device.pin_long)
        self.assertEqual(device['radius'], 500)

    def test_adding_same_locations_to_device(self):
        loc_1 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_2 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)

        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        device = response.json()

        self.assertEqual(device['locations'][0]['id'], loc_2.id)
        self.assertEqual(device['locations'][0]['distance'], loc_2.distance)
        self.assertEqual(device['locations'][1]['id'], loc_1.id)
        self.assertEqual(device['locations'][0]['distance'], loc_1.distance)

#
#     def test_single_device_history(self):
#         # Get a history of the location of the device
#         None
#
#     def test_update_device_location(self):
#         response = self.client.post(f'/api/v1/devices/{self.device.id}', {'location': '[36.996663, -103.234930]'}, format='json')
#         device = response.json()
#
#         self.assertEqual(device['id'], self.device.id)
