from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import User
import json


# Create your tests here.
class UserEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.thrasher = User.objects.create(username='Thrasher',
                                            phone_number='7196639883',
                                            device_number='7192710056')
        self.fluffy = User.objects.create(username='Fluffy',
                                          phone_number='7198839888',
                                          device_number='7192710055')

    def test_create_endpoint(self):
        response = self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888', 'device_number': '7194447777'}}, format='json')
        user = response.json()

        self.assertEqual(user['username'], 'Thor')
        self.assertEqual(user['phone_number'], '7195558888')
        self.assertEqual(user['device_number'], '7194447777')
        self.assertEqual(user['radius'], 5)
