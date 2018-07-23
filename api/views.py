from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from api.models import Device, User
from api.serializers import DeviceSerializer, UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json

from IPython import embed


class UserViews(viewsets.ViewSet):

    def create(self, request):
        user_attrs = request.data['user']
        if 'username' in user_attrs.keys() and 'phone_number' in user_attrs.keys():
            user = User.objects.create(username=user_attrs['username'], phone_number=user_attrs['phone_number'])
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, user_id=None):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def update(self, request, user_id=None):
        user = self.__user_update__(request, user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, user_id=None):
        user = self.__user_update__(request, user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, user_id=None):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def __user_update__(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user_attrs = request.data['user']
        if 'username' in user_attrs.keys():
            user.username = user_attrs['username']
        if 'phone_number' in user_attrs.keys():
            user.phone_number = user_attrs['phone_number']
        if 'device_id' in user_attrs.keys():
            user.device_id = user_attrs['device_id']
        if 'radius' in user_attrs.keys():
            user.radius = user_attrs['radius']
        user.save()
        return user


class DeviceViews(viewsets.ViewSet):

    def retrieve(self, request, device_id=None):
        device = get_object_or_404(Device, id=device_id)
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)

    def update_location(self, request, device_id=None):
        print(f'Here is the request information: {request.data}')
        device = get_object_or_404(Device, id=device_id)
        new_location = request.data['location']
        if new_location != device.location_1:
            device.update_location(new_location)
        device.save()
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)
