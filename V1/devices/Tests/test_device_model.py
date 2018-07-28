from django.test import TestCase
from V1.devices.models import Device
from V1.users.models import User
from V1.locations.models import Location

# python manage.py test V1/devices/tests

class DeviceModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='+17196639883',)
        device = Device.objects.create(user=user,
                              sms_number='+17192710056',
                              pin_lat=39.996665,
                              pin_long=-105.234931)
        Location.objects.create(device=device, lat=39.996292, long=-105.23503)
        Location.objects.create(device=device, lat=39.996292, long=-105.23503)

        count = Device.objects.count()

        self.assertEqual(device.sms_number, '+17192710056')
        self.assertEqual(device.user.id, user.id)
        self.assertEqual(device.pin_lat, 39.996665)
        self.assertEqual(device.pin_long, -105.234931)
        self.assertEqual(count, 1)


    def test_additional_device_saves_to_db(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='+17196639883',)
        Device.objects.create(user=user,
                              sms_number='+17192710056',
                              pin_lat=39.996665,
                              pin_long=-105.234931)
        first_count = Device.objects.count()

        Device.objects.create(user=user,
                              sms_number='+17196639883',
                              pin_lat=22.996665,
                              pin_long=-65.234931)
        device = Device.objects.last()

        second_count = Device.objects.count()

        self.assertEqual(device.sms_number, '+17196639883')
        self.assertEqual(device.pin_lat, 22.996665)
        self.assertEqual(device.pin_long, -65.234931)
        self.assertEqual(device.user.id, user.id)
        self.assertEqual(first_count, 1)
        self.assertEqual(second_count, 2)

    def test_location_saves_to_device(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='+17196639883',)
        device = Device.objects.create(user=user,
                              sms_number='+17192710056',
                              pin_lat=39.996665,
                              pin_long=-105.234931)
        loc_1 = Location.objects.create(device=device, lat=39.996292, long=-105.23503)
        loc_2 = Location.objects.create(device=device, lat=39.996292, long=-105.23503)

        self.assertEqual(device.locations.last().id, loc_1.id)
        self.assertEqual(device.locations.last().lat, 39.996292)
        self.assertEqual(device.locations.last().long, -105.23503)
        self.assertEqual(device.locations.first().id, loc_2.id)
        self.assertEqual(device.locations.first().lat, 39.996292)
        self.assertEqual(device.locations.first().long, -105.23503)

    def test_location_saves_to_device(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='+17196639883',)
        device = Device.objects.create(user=user,
                              sms_number='+17192710056',
                              pin_lat=39.996665,
                              pin_long=-105.234931)
        loc_1 = Location.objects.create(device=device, lat=39.996292, long=-105.23503)
        loc_2 = Location.objects.create(device=device, lat=39.996292, long=-105.23503)

        last_location = device.latest_location()

        self.assertEqual(last_location.id, loc_2.id)
        self.assertEqual(last_location.lat, 39.996292)
        self.assertEqual(last_location.long, -105.23503)
