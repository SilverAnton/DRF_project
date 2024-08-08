from rest_framework.serializers import ModelSerializer
from users.models import Payment
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone", "avatar", "country",)


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

