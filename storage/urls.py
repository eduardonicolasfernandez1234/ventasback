from django.urls import include, re_path
from rest_framework import routers

from storage.api import ProviderViewSet, CategoryViewSet, ProductViewSet, InventoryViewSet

router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'inventory', InventoryViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
