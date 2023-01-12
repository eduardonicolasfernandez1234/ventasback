from rest_framework import serializers, viewsets

from ventasback.models import MyPageNumberPagination
from sales.models import Tax

class TaxSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=255, required=True)
    # percentage = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model = Tax
        field = '__all__'

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    pagination_class = MyPageNumberPagination