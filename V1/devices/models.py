from django.db import models
from V1.users.models import User


class Device(models.Model):
    sms_number = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
