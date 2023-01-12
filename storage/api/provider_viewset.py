from rest_framework import serializers, viewsets
from storage.models import Provider
from ventasback.models import MyPageNumberPagination

class ProviderSerializer(serializers.Serializer):
    
    class Meta:
        model = Provider
        field = '__all__'

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    pagination_class = MyPageNumberPagination