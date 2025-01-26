from rest_framework import serializers
from .models import RiskMetric
from hedgefunds.models import Portfolio


class RiskMetricPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['name']


class RiskMetricSerializer(serializers.ModelSerializer):
    portfolio = RiskMetricPortfolioSerializer()

    class Meta:
        model = RiskMetric
        fields = "__all__"
