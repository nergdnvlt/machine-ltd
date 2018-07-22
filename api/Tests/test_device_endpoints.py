from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Device
import json

from IPython import embed

class DeviceEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.device = Device.objects.create(sms_number='7192710056',
                                            location_1='[39.996665, -105.234931]',
                                            location_2='[39.996664, -105.234930]',
                                            location_3='[39.996663, -105.234930]',)

    def test_single_device_retrieve(self):
        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['location_1'], self.device.location_1)
        self.assertEqual(device['location_2'], self.device.location_2)
        self.assertEqual(device['location_3'], self.device.location_3)

    def test_update_device_location(self):
        response = self.client.post(f'/api/v1/devices/{self.device.id}', {'location': '[36.996663, -103.234930]'}, format='json')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['sms_number'], self.device.sms_number)
        self.assertEqual(device['location_1'], '[36.996663, -103.234930]')
        self.assertEqual(device['location_2'], '[39.996665, -105.234931]')
        self.assertEqual(device['location_3'], '[39.996664, -105.234930]')
