from django.db import models

class Device(models.Model):
    sms_number = models.CharField(max_length=100, null=True)
    location_1 = models.CharField(max_length=300, null=True)
    location_2 = models.CharField(max_length=300, null=True)
    location_3 = models.CharField(max_length=300, null=True)

    def update_location(self, new_location):
        old_loc_1 = self.location_1
        old_loc_2 = self.location_2
        self.location_1 = new_location
        self.location_2 = old_loc_1
        self.location_3 = old_loc_2
        return self


class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    radius = models.FloatField(default=5)
