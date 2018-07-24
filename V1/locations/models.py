from django.db import models
from django.utils import timezone
from V1.users.models import User
from V1.devices.models import Device

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
