from django.db import models
from django.utils import timezone
from geopy.distance import geodesic
from V1.devices.models import Device

class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    lat = models.FloatField()
    long = models.FloatField()
    distance = models.FloatField(null=True)
    timestamp = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.__distance_calc__()
        if not self.id:
            self.timestamp = timezone.now()
        return super(Location, self).save(*args, **kwargs)


    def __distance_calc__(self):
        pin_cord = (self.device.pin_lat, self.device.pin_long)
        cord = (self.lat, self.long)
        self.distance = geodesic(pin_cord, cord).meters
