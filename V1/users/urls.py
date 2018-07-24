from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from V1.users.views import UserViews

urlpatterns = [
    path('', UserViews.as_view({'post': 'create'})),
    path('<user_id>', UserViews.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'patch': 'partial_update',
                                                  'delete': 'destroy'})),
]
