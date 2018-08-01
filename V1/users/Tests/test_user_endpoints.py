from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from V1.users.models import User
from V1.devices.models import Device
import json

# python manage.py test V1/users/tests
class UserEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.thrasher = User.objects.create(username='Thrasher',
                                            phone_number='+17196639883',)
        self.fluffy = User.objects.create(username='Fluffy',
                                          phone_number='+17198839888',)
        self.dev_1 = Device.objects.create(user=self.thrasher,
                                           pin_lat=39.996665,
                                           pin_long=-105.234931)
        self.dev_2 = Device.objects.create(user=self.thrasher,
                                           pin_lat=38.996665,
                                           pin_long=-104.234931)


    def test_user_create_endpoint(self):
        user = {
            "username": "Thor",
            "phone_number": "+17196639883"
        }
        response = self.client.post('/api/v1/users/', user, format='json')
        user = response.json()

        self.assertEqual(user['username'], 'Thor')
        self.assertEqual(user['phone_number'], '+17196639883')


    def test_user_create_endpoint_without_username(self):
        user = {
            "phone_number": "+17196639883"
        }
        response = self.client.post('/api/v1/users/', user, format='json')
        user = response.json()

        self.assertEqual(response.status_code, 400)


    def test_user_create_endpoint_without_phone_number(self):
        user = {
            "username": "Thrasher",
        }
        response = self.client.post('/api/v1/users/', user, format='json')
        user = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_get_user_endpoint(self):
        response = self.client.get(f'/api/v1/users/{self.thrasher.id}')
        user = response.json()

        self.assertEqual(user['username'], 'Thrasher')
        self.assertEqual(user['phone_number'], '+17196639883')
        self.assertEqual(user['devices'][0]['id'], self.dev_1.id )


    def test_get_another_user_endpoint(self):
        response = self.client.get(f'/api/v1/users/{self.fluffy.id}')
        user = response.json()

        self.assertEqual(user['username'], 'Fluffy')
        self.assertEqual(user['phone_number'], '+17198839888')


    def test_get_single_user_sad_path_endpoint(self):
        response = self.client.get('/api/v1/users/10001')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_put_user_endpoint(self):
        db_user = User.objects.create(username="KingWombat", phone_number="+17192710056")

        user = {
            "username": "Odin",
            "phone_number": "+17196639883"

        }

        response = self.client.put(f'/api/v1/users/{db_user.id}', user, format='json')
        end_user = response.json()

        self.assertEqual(end_user['username'], 'Odin')
        self.assertEqual(end_user['phone_number'], '+17196639883')


    def test_put_user_endpoint_no_username(self):
        db_user = User.objects.create(username="Thor", phone_number="+17195558888")
        user = {
            "phone_number": "+17192710056"
        }
        response = self.client.put(f'/api/v1/users/{db_user.id}', user, format='json')
        end_user = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_putput_user_endpoint_no_phone(self):
        db_user = User.objects.create(username="Thor", phone_number="+17195558888")
        user = {
            "username": "Thrasher",
        }
        response = self.client.put(f'/api/v1/users/{db_user.id}', user, format='json')
        end_user = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_sad_path_put_user_endpoint(self):
        response = self.client.put('/api/v1/users/10001', {'user': {'username': 'Thor', 'phone_number': '+17195558888'}}, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_patch_user_endpoint(self):
        db_user = User.objects.create(username="Thor", phone_number="+17195558888")
        user = {
            "username": "Thor",
            "phone_number": "+17192710056"
        }
        response = self.client.patch(f'/api/v1/users/{db_user.id}', user, format='json')
        end_user = response.json()

        self.assertEqual(end_user['phone_number'], '+17192710056')


    def test_patch_user_endpoint_no_username(self):
        db_user = User.objects.create(username="Thor", phone_number="+17195558888")
        user = {
            "phone_number": "+17192710056"
        }
        response = self.client.patch(f'/api/v1/users/{db_user.id}', user, format='json')
        end_user = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_patch_user_endpoint_no_phone(self):
        db_user = User.objects.create(username="Thor", phone_number="+17195558888")
        user = {
            "username": "Thrasher",
        }
        response = self.client.patch(f'/api/v1/users/{db_user.id}', user, format='json')
        end_user = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_sad_path_patch_user_endpoint(self):
        response = self.client.patch('/api/v1/users/10001', {'user': {'username': 'Thor', 'phone_number': '+17192291210'}}, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_user_endpoint(self):
        self.client.post('/api/v1/users/', {'user': {'username': 'Thor', 'phone_number': '+17195558888'}}, format='json')
        user_id = User.objects.last().id

        response = self.client.delete(f'/api/v1/users/{user_id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_sad_path_delete_user_endpoint(self):
        response = self.client.delete(f'/api/v1/users/10001')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_user_devices_index_endpoint(self):
        response = self.client.get(f'/api/v1/users/{self.thrasher.id}/devices')
        devices = response.json()

        self.assertEqual(devices[0]['id'], self.dev_1.id )
        self.assertEqual(devices[1]['id'], self.dev_2.id )
