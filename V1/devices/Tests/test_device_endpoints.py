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
        loc_3 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_4 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)

        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        device = response.json()

        self.assertEqual(device['last_location']['id'], loc_4.id)
        self.assertEqual(device['last_location']['distance'], loc_4.distance)
        self.assertEqual((loc_1.id in device['last_location'].values()), False)
        self.assertEqual((loc_2.id in device['last_location'].values()), False)
        self.assertEqual((loc_3.id in device['last_location'].values()), False)

    def test_update_device_location(self):
        loc_1 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_2 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_3 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)

        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        first_device = response.json()

        self.assertEqual(first_device['last_location']['id'], loc_3.id)
        self.assertEqual(first_device['last_location']['distance'], loc_3.distance)

        loc_4 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)

        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        last_device_response = response.json()

        self.assertEqual(last_device_response['last_location']['id'], loc_4.id)
        self.assertEqual(last_device_response['last_location']['distance'], loc_4.distance)

    def test_history_of_device_location(self):
        loc_1 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_2 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_3 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)
        loc_4 = Location.objects.create(device=self.device, lat=39.996292, long=-105.23503)

        response = self.client.get(f'/api/v1/devices/{self.device.id}/history')
        history = response.json()

        self.assertEqual(history[0]['id'], loc_4.id)
        self.assertEqual(history[0]['lat'], loc_4.lat)
        self.assertEqual(history[0]['long'], loc_4.long)
        self.assertEqual(history[0]['distance'], loc_4.distance)
        self.assertEqual(history[1]['id'], loc_3.id)
        self.assertEqual(history[1]['lat'], loc_3.lat)
        self.assertEqual(history[1]['long'], loc_3.long)
        self.assertEqual(history[1]['distance'], loc_3.distance)
        self.assertEqual(history[2]['id'], loc_2.id)
        self.assertEqual(history[2]['lat'], loc_2.lat)
        self.assertEqual(history[2]['long'], loc_2.long)
        self.assertEqual(history[2]['distance'], loc_2.distance)
        self.assertEqual(history[3]['id'], loc_1.id)
        self.assertEqual(history[3]['lat'], loc_1.lat)
        self.assertEqual(history[3]['long'], loc_1.long)
        self.assertEqual(history[3]['distance'], loc_1.distance)

    def test_post_location_to_device(self):
        response = self.client.post(f'/api/v1/devices/{self.device.id}', { 'location': [39.996291, -105.23502] }, format='json')
        device = response.json()
        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['last_location']['lat'], 39.996291)
        self.assertEqual(device['last_location']['long'], -105.23502)
