from django.db import models
from V1.devices.models import Device

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

    def update_user(self, user_attrs):
        if 'username' in user_attrs.keys():
            self.username = user_attrs['username']
        if 'phone_number' in user_attrs.keys():
            self.phone_number = user_attrs['phone_number']
        if 'device_id' in user_attrs.keys():
            self.device_id = user_attrs['device_id']
        self.save()
        return self
