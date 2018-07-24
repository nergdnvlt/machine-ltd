from django.test import TestCase
from V1.locations.models import Location
from V1.devices.models import Device

# python manage.py test V1/locations/tests

class LocationModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        device = Device.objects.create(sms_number='7192710056')

        input_location = Location.objects.create(user=user, device=device, location='[39.996665, -105.234931]')

        saved_location = Location.objects.first()
        count = Location.objects.count()

        self.assertEqual(saved_location.location, '[39.996665, -105.234931]')
        self.assertEqual(saved_location.user.id, user.id)
        self.assertEqual(saved_location.device.id, device.id)
        self.assertEqual(saved_location.radius, 500)
        self.assertEqual(count, 1)
