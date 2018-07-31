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

class SessionViews(viewsets.ViewSet):

    def create(self, request):
        username = request.data['username']
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, many=False)
        return Response({"user": serializer.data, "session": True}, status=status.HTTP_200_OK)
