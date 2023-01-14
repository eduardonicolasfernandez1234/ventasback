from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from base.models import MyPageNumberPagination
from storage.models import Inventory, Product, Provider, Category
from storage.api import ProductSerializer, ProviderSerializer, InventoryFilterSerializer


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

    @action(detail=True, methods=['get'], url_path="category",
            name="get all products of inventory by category id")
    def inventory_list_by_category(self, request, pk=None):
        if pk is None:
            return Response({
                "detail": "Missing foreign key",
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({
                "detail": "Category not found",
            }, status=status.HTTP_404_NOT_FOUND)

        queryset = Inventory.objects.filter(product__category_id=pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = InventorySerializer(page, many=True, read_only=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = InventorySerializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="provider",
            name="get all products of inventory by provider id")
    def inventory_list_by_provider(self, request, pk=None):
        if pk is None:
            return Response({
                "detail": "Missing foreign key",
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response({
                "detail": "Provider not found",
            }, status=status.HTTP_404_NOT_FOUND)

        queryset = Inventory.objects.filter(provider_id=pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = InventorySerializer(page, many=True, read_only=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = InventorySerializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path="search",
            name="get all products of inventory by fields")
    def inventory_list_filtered(self, request, pk=None):
        serializer = InventoryFilterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        queryset = Inventory.objects.all()
        if serializer['price_init'].value is not None and serializer['price_last'].value is not None:
            queryset = queryset.filter(
                price__gte=serializer['price_init'].value,
                price__lte=serializer['price_last'].value
            )
        if serializer['stock_init'].value is not None and serializer['stock_last'].value is not None:
            queryset = queryset.filter(
                stock__gte=serializer['stock_init'].value,
                stock__lte=serializer['stock_last'].value
            )
        if serializer['provider'].value is not None:
            queryset = queryset.filter(
                provider__name__icontains=serializer['provider'].value
            )
        if serializer['category'].value is not None:
            queryset = queryset.filter(
                product__category__name__icontains=serializer['category'].value
            )
        if serializer['product'].value is not None:
            queryset = queryset.filter(
                product__name__icontains=serializer['product'].value
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = InventorySerializer(page, many=True, read_only=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = InventorySerializer(queryset, many=True)
            return Response(serializer.data)
