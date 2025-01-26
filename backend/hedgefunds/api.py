from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fund
from .serializers import FundsAllSerializer
from drf_yasg.utils import swagger_auto_schema


class FundsApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all funds", responses={200: FundsAllSerializer(many=True)})
    def get(self, request):
        funds = Fund.objects.all()
        serializer = FundsAllSerializer(funds, many=True)
        return Response(serializer.data)
