from rest_framework import serializers
from .models import Fund, HedgeFundCompany


class HedgeFundCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = HedgeFundCompany
        fields = '__all__'


class FundsAllSerializer(serializers.ModelSerializer):
    hedge_fund_company = HedgeFundCompanySerializer()

    class Meta:
        model = Fund
        fields = '__all__'
