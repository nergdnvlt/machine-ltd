from django.db import models


class Device(models.Model):
    location_1 = models.CharField(max_length=300)
    location_2 = models.CharField(max_length=300)
    location_3 = models.CharField(max_length=300)
    location_4 = models.CharField(max_length=300)
    location_5 = models.CharField(max_length=300)
