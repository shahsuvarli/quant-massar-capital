from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import RiskMetric
from .serializers import RiskMetricSerializer


class RiskMetricApiView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all risk metrics",
        responses={200: RiskMetricSerializer(many=True)}
    )
    def get(self, request):
        # Get the user's risk metrics
        risk_metrics = RiskMetric.objects.all()[0:20]
        serializer = RiskMetricSerializer(risk_metrics, many=True)
        return Response(serializer.data)
