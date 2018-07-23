from django.db import models
from django.utils import timezone


class Device(models.Model):
    sms_number = models.CharField(max_length=100, null=True)

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


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=300, null=True)
    timestamp = models.DateTimeField(null=True)
    radius = models.IntegerField(default=500)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        return super(Location, self).save(*args, **kwargs)
