from django.db import models
from V1.users.models import User

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sms_number = models.CharField(max_length=100, null=True)
    radius = models.IntegerField(default=500)
    pin_lat = models.FloatField()
    pin_long = models.FloatField()

    def latest_location(self):
        return self.locations.first()

    class Meta:
        db_table = 'devices'
