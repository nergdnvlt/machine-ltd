from twilio.rest import Client
from service_objects.services import Service
from django.conf import settings

class TwilioService(Service):

    def __init__(self):
        self.twilio_sid = settings.TWILIO_SID
        self.twilio_token = settings.TWILIO_AUTH
        self.client = Client(self.twilio_sid, self.twilio_token)

    def send_sms(self, number, lat, long):
        url = f'http://maps.google.com/?q={lat},{long}'
        message = self.client.messages.create(
            to=number,
            from_='+17205130638',
            body=f'Moving asset. Location: lattitude: {lat}, and longitude {long}. {url}'
        )
        return message.body
