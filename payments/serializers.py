from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from payments.models import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
