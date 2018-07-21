from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DeviceViews, UserViews

urlpatterns = [
    path('v1/users/', UserViews.as_view({'post': 'create'})),
    path('v1/users/<user_id>', UserViews.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'patch': 'partial_update',
                                                  'delete': 'destroy'})),
    path('v1/devices/<device_id>', DeviceViews.as_view({'get': 'retrieve',
                                                        'post': 'update_location'})),
]
