from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DeviceViews

urlpatterns = [
    path('v1/devices/<device_id>', DeviceViews.as_view({'get': 'retrieve',
                                                        'put': 'update'})),
]
