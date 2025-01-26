from .models import PaymentInfo
from accounts.serializers import UserSerializer
from rest_framework import serializers
from accounts.models import User


class PaymentInfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PaymentInfoSerializer(serializers.ModelSerializer):
    user = PaymentInfoUserSerializer()

    class Meta:
        model = PaymentInfo
        fields = "__all__"
