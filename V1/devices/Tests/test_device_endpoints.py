from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from V1.devices.models import Device
import json

# python manage.py test V1/devices/tests


class DeviceEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.device = Device.objects.create(sms_number='7192710056')

    def test_single_device_retrieve(self):
        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['sms_number'], self.device.sms_number)

    def test_single_device_history(self):
        # Get a history of the location of the device
        None

    # def test_update_device_location(self):
    #     response = self.client.post(f'/api/v1/devices/{self.device.id}', {'location': '[36.996663, -103.234930]'}, format='json')
    #     device = response.json()
    #
    #     self.assertEqual(device['id'], self.device.id)
