from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from V1.users.views import UserViews
from V1.devices.views import DeviceViews

urlpatterns = [
    path('', UserViews.as_view({
        'post': 'create'
    })),
    path('<username>', UserViews.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('<username>/devices', DeviceViews.as_view({
        'get': 'list',
        'post': 'create',
    })),
]
