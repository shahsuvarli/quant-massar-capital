from rest_framework import serializers
from .models import Fund, HedgeFundCompany, Portfolio
from accounts.serializers import UserSerializer


class HedgeFundCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = HedgeFundCompany
        fields = '__all__'


class FundsAllSerializer(serializers.ModelSerializer):
    hedge_fund_company = HedgeFundCompanySerializer()

    class Meta:
        model = Fund
        fields = '__all__'

class PortfolioFundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = '__all__'

class PortfolioAllSerializer(serializers.ModelSerializer):
    fund = PortfolioFundSerializer()
    manager = UserSerializer()

    class Meta:
        model = Portfolio
        fields = '__all__'