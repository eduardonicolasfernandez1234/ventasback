# from django.conf.urls import url
from django.urls import include, re_path
from rest_framework import routers

from sales.api import TaxViewSet, OrderViewSet, ConfigSalesViewSet, SalesViewSet

router = routers.DefaultRouter()
router.register(r'tax', TaxViewSet)
router.register(r'order', OrderViewSet)
router.register(r'config-sales', ConfigSalesViewSet)
router.register(r'sales', SalesViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]