from rest_framework import serializers

class UserCreateSimpleSerializer(serializers.Serializer):
    
    user_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=30)
    full_name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    phone = serializers.CharField(max_length=10)
    nit = serializers.CharField(max_length=13)
    birth_date = serializers.DateField(required=False)

    class Meta:
        fields = '__all__'