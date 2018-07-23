from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Device, User, Location
import json

from IPython import embed

class LocationModelTest(TestCase):

    def test_location_saves_to_db_with_default_radius(self):
        device = Device.objects.create(sms_number='7196639883')
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        location = Location.objects.create(device=device, user=user,
                                           location='[39.996665, -105.234931]')

        beacon = Location.objects.first()
        count = Device.objects.count()

        self.assertEqual(beacon.location, location.location)
        self.assertEqual(beacon.device.id, device.id)
        self.assertEqual(beacon.user.id, user.id)
        self.assertEqual(beacon.radius, 500)
        self.assertEqual(count, 1)

    def test_location_saves_to_db(self):
        device = Device.objects.create(sms_number='7196639883')
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        location = Location.objects.create(device=device, user=user,
                                           location='[39.996665, -105.234931]',
                                           radius=1000)

        beacon = Location.objects.first()
        count = Device.objects.count()

        self.assertEqual(beacon.location, location.location)
        self.assertEqual(beacon.device.id, device.id)
        self.assertEqual(beacon.user.id, user.id)
        self.assertEqual(beacon.radius, 1000)
        self.assertEqual(count, 1)
