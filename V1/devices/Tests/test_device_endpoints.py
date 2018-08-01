from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from V1.devices.models import Device
from V1.users.models import User
from V1.locations.models import Location
import json

# python manage.py test V1/devices/tests
class DeviceEndpointTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.thrasher = User.objects.create(username='Thrasher',
                                   phone_number='+17196639883',)
        self.device = Device.objects.create(user=self.thrasher,
                                            pin_lat=39.996292,
                                            pin_long=-105.23503)


    def test_single_device_retrieve(self):
        response = self.client.get(f'/api/v1/devices/{self.device.id}')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['pin_lat'], self.device.pin_lat)
        self.assertEqual(device['pin_long'], self.device.pin_long)
        self.assertEqual(device['radius'], 500)


    def test_create_device(self):
        user = User.objects.create(username="Fluffy", phone_number="+17196639883")
        device = {
            "pin_lat": "39.996292",
            "pin_long": "-105.23503"
        }
        response = self.client.post(f'/api/v1/users/{user.id}/devices', device, format='json')
        res_device = response.json()
        end_device = Device.objects.last()

        self.assertEqual(res_device['id'], end_device.id)
        self.assertEqual(res_device['pin_lat'], end_device.pin_lat)
        self.assertEqual(res_device['pin_long'], end_device.pin_long)
        self.assertEqual(res_device['radius'], end_device.radius)


    def test_update_device(self):
        up_device = {
            "pin_lat": "39.996292",
            "pin_long": "-105.23503",
            "radius": '1000',
        }
        response = self.client.put(f'/api/v1/devices/{self.device.id}', up_device, format='json')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['pin_lat'], self.device.pin_lat)
        self.assertEqual(device['pin_long'], self.device.pin_long)
        self.assertEqual(device['radius'], 1000.0)


    def test_patch_update_device(self):
        up_device = {
            "pin_lat": "39.996292",
            "pin_long": "-105.23503",
            "radius": '1000',
        }
        response = self.client.put(f'/api/v1/devices/{self.device.id}', up_device, format='json')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['pin_lat'], self.device.pin_lat)
        self.assertEqual(device['pin_long'], self.device.pin_long)
        self.assertEqual(device['radius'], 1000.0)


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
        location = {
            "lat": "39.996291",
            "long": "-105.23502"
        }
        response = self.client.post(f'/api/v1/devices/{self.device.id}/locations', location, format='json')
        device = response.json()

        self.assertEqual(device['id'], self.device.id)
        self.assertEqual(device['last_location']['lat'], 39.996291)
        self.assertEqual(device['last_location']['long'], -105.23502)


    def test_alert_if_location_greater_than_radius_when_alert_active(self):
        response = self.client.post(f'/api/v1/devices/{self.device.id}/locations', {"lat": "39.999291", "long": "-105.25802"}, format='json')
        device = response.json()
        self.assertTrue(device['device']['last_location']['distance'] > device['device']['radius'])
        self.assertEqual(device['message'], "Sent from your Twilio trial account - Moving asset. Location: latitude: 39.999291, and longitude -105.25802. http://maps.google.com/?q=39.999291,-105.25802")


    def test_alert_if_location_greater_than_radius_when_alert_not_active(self):
        start_device = Device.objects.create(
            pin_lat=39.996292,
            pin_long=-105.23503,
            alert=False,
            user=self.thrasher
        )
        response = self.client.post(f'/api/v1/devices/{start_device.id}/locations', {"lat": "39.999291", "long": "-105.25802"}, format='json')
        device = response.json()
        self.assertTrue(device['last_location']['distance'] > device['radius'])


    def test_delete_device_endpoint(self):
        thrasher_2 = User.objects.create(username='Ichibod',
                                   phone_number='+17196639883',)

        response = self.client.delete(f'/api/v1/devices/{thrasher_2.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_sad_path_delete_user_endpoint(self):
        response = self.client.delete(f'/api/v1/devices/10001')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
