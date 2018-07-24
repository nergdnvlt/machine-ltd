from django.test import TestCase
from V1.devices.models import Device
from V1.users.models import User

from IPython import embed

# python manage.py test V1/devices/tests

class DeviceModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        Device.objects.create(user=user,
                              sms_number='7192710056',
                              pin_lat=39.996665,
                              pin_long=-105.234931)

        device = Device.objects.get(sms_number='7192710056')
        count = Device.objects.count()

        self.assertEqual(device.sms_number, '7192710056')
        self.assertEqual(device.user.id, user.id)
        self.assertEqual(device.pin_lat, 39.996665)
        self.assertEqual(device.pin_long, -105.234931)
        self.assertEqual(count, 1)


    # def test_additional_device_saves_to_db(self):
    #     user = User.objects.create(username='Thrasher',
    #                                phone_number='7196639883',)
    #     Device.objects.create(user=user, sms_number='7192710056')
    #     first_count = Device.objects.count()
    #
    #     second_user = User.objects.create(username='Thrasher',
    #                                phone_number='7196639883',)
    #     Device.objects.create(user=second_user, sms_number='7196639883')
    #     device = Device.objects.last()
    #
    #     second_count = Device.objects.count()
    #
    #     self.assertEqual(device.sms_number, '7196639883')
    #     self.assertEqual(first_count, 1)
    #     self.assertEqual(second_count, 2)
