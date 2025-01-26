from .models import Instrument, Trade
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InstrumentSerializer, TradeSerializer
from drf_yasg.utils import swagger_auto_schema

class intrumentsApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all instruments", responses={200: InstrumentSerializer(many=True)})
    def get(self, request):
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)


class TradesApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all trades", responses={200: TradeSerializer(many=True)})
    def get(self, request):
        trades = Trade.objects.all()[:10]
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)