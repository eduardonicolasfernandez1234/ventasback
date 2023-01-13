from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from ventasback.models import MyPageNumberPagination
from storage.models import Inventory, Product, Provider
from storage.api import ProductSerializer, ProviderSerializer

class InventorySerializer(serializers.ModelSerializer):
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
        fields = '__all__'

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    pagination_class = MyPageNumberPagination
    
    def create(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inventory = serializer.save()
        inventory.stock = inventory.quantity
        inventory = inventory.save()
        headers = self.get_success_headers(inventory)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)