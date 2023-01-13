# from rest_framework import serializers
# from sales.models import Sales, Order

# class SimpleSalesSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Sales
#         fields = '__all__'
    
# class SimpleOrderSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Order
#         fields = '__all__'

# class CreateSalesSerializer(serializers.Serializer):
#     sales = SimpleSalesSerializer(write_only=True, many=False)
#     orders = SimpleOrderSerializer(write_only=True, many=True)
