from .models import Instrument, Trade
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InstrumentSerializer, TradeSerializer, TradeCreateSerializer
from drf_yasg.utils import swagger_auto_schema


class IntrumentsApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all instruments", responses={200: InstrumentSerializer(many=True)})
    def get(self, request):
        instruments = Instrument.objects.order_by("name")[0:20]
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)


class TradesApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all trades", responses={200: TradeSerializer(many=True)})
    def get(self, request):
        trades = Trade.objects.order_by("-executed_at")[0:20]
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)


class TradeApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve trade by id", responses={200: TradeSerializer})
    def get(self, request, trade_id):
        trade = Trade.objects.get(id=trade_id)
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Create a trade", request_body=TradeCreateSerializer, responses={200: TradeCreateSerializer})
    def post(self, request):
        serializer = TradeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
