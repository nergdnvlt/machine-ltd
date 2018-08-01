from django.db import models
from django.utils.text import slugify

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
