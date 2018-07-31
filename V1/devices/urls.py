from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from V1.devices.views import DeviceViews
from V1.locations.views import LocationViews

urlpatterns = [
    path('<device_id>', DeviceViews.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
    })),
    path('<device_id>/locations', LocationViews.as_view({
        'post': 'create',
    })),
    path('<device_id>/history', LocationViews.as_view({
        'get': 'index',
    })),
]
