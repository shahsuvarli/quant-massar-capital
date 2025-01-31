from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fund, Portfolio, HedgeFundCompany
from .serializers import FundsAllSerializer, PortfolioAllSerializer, HedgeFundCompanySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from trading.models import Trade
import numpy as np


class FundsApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all funds", responses={200: FundsAllSerializer(many=True)})
    def get(self, request):
        funds = Fund.objects.order_by("-inception_date")[0:20]
        serializer = FundsAllSerializer(funds, many=True)
        return Response(serializer.data)


class PortfoliosApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all portfolios", responses={200: PortfolioAllSerializer(many=True)})
    def get(self, request):
        portfolios = Portfolio.objects.order_by("-created_at")[0:20]
        serializer = PortfolioAllSerializer(portfolios, many=True)
        return Response(serializer.data)


class HedgeFundCompanyApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all hedge fund companies", responses={200: HedgeFundCompanySerializer(many=True)})
    def get(self, request):
        hedge_fund_companies = HedgeFundCompany.objects.order_by(
            "-inception_date")[0:20]
        serializer = HedgeFundCompanySerializer(
            hedge_fund_companies, many=True)
        return Response(serializer.data)
