from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from V1.users.models import User
from V1.users.serializers import UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import json
from IPython import embed

class UserViews(viewsets.ViewSet):

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user.id:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        user.update_user(user_attrs)
        return user
