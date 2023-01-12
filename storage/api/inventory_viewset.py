from rest_framework import serializers, viewsets
from ventasback.models import MyPageNumberPagination
from storage.models import Inventory, Product, Provider
from storage.api import ProductSerializer, ProviderSerializer

class InventorySerializer(serializers.Serializer):
    product = ProductSerializer(read_only=True, many=False)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=Product.objects.all(), source='product'
    )
    provider = ProviderSerializer(read_only=True, many=False)
    provider_id = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, queryset=Provider.objects.all(), source='provider'
    )
    
    class Meta:
        model = Inventory
        field = '__all__'

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    pagination_class = MyPageNumberPagination