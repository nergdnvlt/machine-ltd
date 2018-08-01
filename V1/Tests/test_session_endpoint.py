from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from V1.users.models import User
from V1.devices.models import Device
import json

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
        user_session = response.json()

        self.assertEqual(user_session['session'], True)
        self.assertEqual(user_session['user']['username'], self.thrasher.username)


    def test_user_no_user(self):
        user = {
            "username": "Bob"
        }
        response = self.client.post('/api/v1/sessions', user, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
