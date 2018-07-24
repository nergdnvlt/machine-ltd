from django.db import models
from django.utils import timezone
from V1.devices.models import Device

class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    lat = models.FloatField()
    long = models.FloatField()
    timestamp = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        return super(Location, self).save(*args, **kwargs)
