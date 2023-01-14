from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

import datetime

class MyTokenSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        super().update(instance, validated_data)

    def create(self, validated_data):
        super().create(validated_data)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['user_type'] = user.user_type
        token['email'] = user.email
        token['date'] = str(datetime.date.today())
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenSerializer