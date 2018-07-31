from django.db import models
from V1.users.models import User

class Device(models.Model):
    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    radius = models.FloatField(default=500)
    pin_lat = models.FloatField()
    pin_long = models.FloatField()
    alert = models.BooleanField(default=True)

    def is_active(self):
        return self.alert

    def is_triggered(self):
        return self.radius <= self.locations.first().distance

    def latest_location(self):
        return self.locations.first()

    class Meta:
        db_table = 'devices'
        ordering = ('id',)
