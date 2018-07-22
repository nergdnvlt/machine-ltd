from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import User
import json

class UserEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.thrasher = User.objects.create(username='Thrasher',
                                            phone_number='7196639883',)
        self.fluffy = User.objects.create(username='Fluffy',
                                          phone_number='7198839888',)

    def test_user_create_endpoint(self):
        response = self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888'}}, format='json')
        user = response.json()

        self.assertEqual(user['username'], 'Thor')
        self.assertEqual(user['phone_number'], '7195558888')
        self.assertEqual(user['radius'], 5)

    def test_get_user_endpoint(self):
        response = self.client.get(f'/api/v1/users/{self.thrasher.id}')
        user = response.json()

        self.assertEqual(user['username'], 'Thrasher')
        self.assertEqual(user['phone_number'], '7196639883')
        self.assertEqual(user['radius'], 5.0)

    def test_get_another_user_endpoint(self):
        response = self.client.get(f'/api/v1/users/{self.fluffy.id}')
        user = response.json()

        self.assertEqual(user['username'], 'Fluffy')
        self.assertEqual(user['phone_number'], '7198839888')
        self.assertEqual(user['radius'], 5.0)

    def test_get_single_user_sad_path_endpoint(self):
        response = self.client.get('/api/v1/users/10001')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_endpoint(self):
        self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888'}}, format='json')
        user_id = User.objects.last().id

        response = self.client.put(f'/api/v1/users/{user_id}', {'user': {'username': 'Thor', 'phone_number': '7195558888', 'radius': 10}}, format='json')
        end_user = response.json()

        self.assertEqual(end_user['radius'], 10.0)

    def test_update_user_endpoint(self):
        self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888'}}, format='json')
        user_id = User.objects.last().id

        response = self.client.put(f'/api/v1/users/{user_id}', {'user': {'username': 'Thor', 'phone_number': '7195558888', 'radius': 10}}, format='json')
        end_user = response.json()

        self.assertEqual(end_user['radius'], 10.0)

    def test_put_user_endpoint(self):
        self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888'}}, format='json')
        user_id = User.objects.last().id

        response = self.client.put(f'/api/v1/users/{user_id}', {'user': {'username': 'Thor', 'phone_number': '7195558888', 'radius': 10}}, format='json')
        end_user = response.json()

        self.assertEqual(end_user['radius'], 10.0)

    def test_sad_path_put_user_endpoint(self):
        response = self.client.put('/api/v1/users/10001', {'user': {'username': 'Thor', 'phone_number': '7195558888', 'radius': 10}}, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_user_endpoint(self):
        self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888'}}, format='json')
        user_id = User.objects.last().id

        response = self.client.patch(f'/api/v1/users/{user_id}', {'user': {'radius': 10}}, format='json')
        end_user = response.json()

        self.assertEqual(end_user['radius'], 10.0)

    def test_sad_path_patch_user_endpoint(self):
        response = self.client.patch('/api/v1/users/10001', {'user': {'username': 'Thor', 'phone_number': '7195558888', 'radius': 10}}, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_user_endpoint(self):
        self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '7195558888'}}, format='json')
        user_id = User.objects.last().id

        response = self.client.delete(f'/api/v1/users/{user_id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_sad_path_delete_user_endpoint(self):
        response = self.client.delete(f'/api/v1/users/10001')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
