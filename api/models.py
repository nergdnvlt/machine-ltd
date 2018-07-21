from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    device_number = models.CharField(max_length=100)
    radius = models.FloatField(default=5)



class Device(models.Model):
    sms_number = models.CharField(max_length=100, blank=True)
    location_1 = models.CharField(max_length=300, blank=True)
    location_2 = models.CharField(max_length=300, blank=True)
    location_3 = models.CharField(max_length=300, blank=True)
