from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from V1.devices.views import DeviceViews

urlpatterns = [
    path('<device_id>', DeviceViews.as_view({'get': 'retrieve', 'post': 'update_location'})),
]
