from django.test import TestCase

from api.models import Device

# Create your tests here.
class DeviceModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        Device.objects.create(sms_number='7192710056',
                              location_1='[39.996665, -105.234931]',
                              location_2='[39.996664, -105.234930]',
                              location_3='[39.996663, -105.234930]',)

        device = Device.objects.get(sms_number='7192710056')
        count = Device.objects.count()

        self.assertEqual(device.sms_number, '7192710056')
        self.assertEqual(device.location_1, '[39.996665, -105.234931]')
        self.assertEqual(device.location_2, '[39.996664, -105.234930]')
        self.assertEqual(device.location_3, '[39.996663, -105.234930]')
        self.assertEqual(count, 1)


    def test_additional_device_saves_to_db(self):
        Device.objects.create(sms_number='7192710056',
                              location_1='[39.996665, -105.234931]',
                              location_2='[39.996664, -105.234930]',
                              location_3='[39.996663, -105.234930]',)
        first_count = Device.objects.count()
        Device.objects.create(sms_number='7196639883',
                              location_1='[88.996665, -108.234931]',
                              location_2='[88.996664, -108.234930]',
                              location_3='[88.996663, -108.234930]',)

        device = Device.objects.last()
        second_count = Device.objects.count()

        self.assertEqual(device.sms_number, '7196639883')
        self.assertEqual(device.location_1, '[88.996665, -108.234931]')
        self.assertEqual(device.location_2, '[88.996664, -108.234930]')
        self.assertEqual(device.location_3, '[88.996663, -108.234930]')
        self.assertEqual(first_count, 1)
        self.assertEqual(second_count, 2)
