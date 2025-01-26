from .models import Instrument, Trade
from rest_framework import serializers
from hedgefunds.serializers import PortfolioAllSerializer
from hedgefunds.models import Portfolio


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class TradePortfolioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Portfolio
        fields = '__all__'

class TradeSerializer(serializers.ModelSerializer):
    portfolio = TradePortfolioSerializer()
    instrument = InstrumentSerializer()

    class Meta:
        model = Trade
        fields = '__all__'
