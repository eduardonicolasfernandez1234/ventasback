from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.models import User
from authentication.api import UserCreateSimpleSerializer

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'is_active', 'is_staff', 
                 'is_superuser', 'user_type', 'address', 'email', 'phone', 'nit', 'birth_date']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    @action(detail=False, url_path='client', methods=['post'], description='Insert user type client')
    def insert_client(self, request, pk=None):
        try:
            serializer = UserCreateSimpleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_data = serializer.data
        user = User.objects.create_user(
            full_name=user_data['full_name'],
            address=user_data['address'],
            email=user_data['email'],
            username=user_data['username'],
            password=user_data['password'],
            phone=user_data['phone'],
            nit=user_data['nit'],
            birth_date=user_data['birth_date'],
            user_type=User.TYPE_CLIENT,
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, url_path='supervisor', methods=['post'], description='Insert user type supervisor')
    def insert_supervisor(self, request, pk=None):
        try:
            serializer = UserCreateSimpleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_data = serializer.data
        user = User.objects.create_user(
            full_name=user_data['full_name'],
            address=user_data['address'],
            email=user_data['email'],
            username=user_data['username'],
            password=user_data['password'],
            phone=user_data['phone'],
            nit=user_data['nit'],
            birth_date=user_data['birth_date'],
            user_type=User.TYPE_SUPERVISOR,
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, url_path='admin', methods=['post'], description='Insert user type admin')
    def insert_admin(self, request, pk=None):
        try:
            serializer = UserCreateSimpleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_data = serializer.data
        user = User.objects.create_user(
            full_name=user_data['full_name'],
            address=user_data['address'],
            email=user_data['email'],
            username=user_data['username'],
            password=user_data['password'],
            phone=user_data['phone'],
            nit=user_data['nit'],
            birth_date=user_data['birth_date'],
            user_type=User.TYPE_ADMIN,
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        