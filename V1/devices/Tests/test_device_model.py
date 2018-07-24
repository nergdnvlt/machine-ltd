from django.test import TestCase
from V1.devices.models import Device

# python manage.py test V1/devices/tests

class DeviceModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        Device.objects.create(sms_number='7192710056')

        device = Device.objects.get(sms_number='7192710056')
        count = Device.objects.count()

        self.assertEqual(device.sms_number, '7192710056')
        self.assertEqual(count, 1)


    def test_additional_device_saves_to_db(self):
        Device.objects.create(sms_number='7192710056')
        first_count = Device.objects.count()
        Device.objects.create(sms_number='7196639883')

        device = Device.objects.last()
        second_count = Device.objects.count()

        self.assertEqual(device.sms_number, '7196639883')
        self.assertEqual(first_count, 1)
        self.assertEqual(second_count, 2)
