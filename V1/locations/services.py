# from service_objects.services import Service
#
# class LocationService(Service):
#
#     def __init__(self):
#         self.twilio_sid = settings.TWILIO_SID
#         self.twilio_token = settings.TWILIO_AUTH
#         self.client = Client(self.twilio_sid, self.twilio_token)
#
#     def add_location(self, request, device_id=None):
#         device = get_object_or_404(Device, id=device_id)
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             location = serializer.save(device=device)
#             if location:
#                 res_serializer = DeviceSerializer(device, many=False)
#                 if device.radius <= location.distance:
#                     message = TwilioService().send_sms(device.user.phone_number, location.lat, location.long)
#                     return Response({"device": res_serializer.data, "message": message}, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(res_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
