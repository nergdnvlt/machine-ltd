from django.db import models

class Device(models.Model):
    sms_number = models.CharField(max_length=100, null=True)
    location_1 = models.CharField(max_length=300, null=True)
    location_2 = models.CharField(max_length=300, null=True)
    location_3 = models.CharField(max_length=300, null=True)
    location_4 = models.CharField(max_length=300, null=True)
    location_5 = models.CharField(max_length=300, null=True)
    location_6 = models.CharField(max_length=300, null=True)
    location_7 = models.CharField(max_length=300, null=True)
    location_8 = models.CharField(max_length=300, null=True)
    location_9 = models.CharField(max_length=300, null=True)
    location_10 = models.CharField(max_length=300, null=True)

    def update_location(self, new_location):
        self.location_10 = self.location_9
        self.location_9 = self.location_8
        self.location_8 = self.location_7
        self.location_7 = self.location_6
        self.location_6 = self.location_5
        self.location_5 = self.location_4
        self.location_4 = self.location_3
        self.location_3 = self.location_2
        self.location_2 = self.location_1
        self.location_1 = new_location
        self.save()
        return self


class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    radius = models.FloatField(default=5)

    def update_user(self, user_attrs):
        if 'username' in user_attrs.keys():
            self.username = user_attrs['username']
        if 'phone_number' in user_attrs.keys():
            self.phone_number = user_attrs['phone_number']
        if 'device_id' in user_attrs.keys():
            self.device_id = user_attrs['device_id']
        if 'radius' in user_attrs.keys():
            self.radius = user_attrs['radius']
        self.save()
        return self
