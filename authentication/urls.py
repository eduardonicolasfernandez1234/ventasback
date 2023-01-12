from django.urls import include, re_path
from rest_framework import routers

from authentication.api import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]