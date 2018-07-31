from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from V1.users.models import User
from V1.devices.models import Device
import json

from IPython import embed

# python manage.py test V1/Tests
class SessionEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.thrasher = User.objects.create(username='Thrasher',
                                            phone_number='+17196639883',)
        self.fluffy = User.objects.create(username='Fluffy',
                                          phone_number='+17198839888',)
        self.dev_1 = Device.objects.create(user=self.thrasher,
                                           pin_lat=39.996665,
                                           pin_long=-105.234931)

    def test_user_can_create_new_session(self):
        user = {
            "username": "Thrasher"
        }
        response = self.client.post('/api/v1/sessions', user, format='json')
        user = response.json()
