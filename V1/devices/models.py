from django.db import models
from django.utils import timezone


class Device(models.Model):
    sms_number = models.CharField(max_length=100, null=True)
