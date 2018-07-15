from mongoengine import *


class Device(Document):
    device_id = IntField(default=0)
    location = StringField(max_length=300)

    class Meta:
        abstract = True
