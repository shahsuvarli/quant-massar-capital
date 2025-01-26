from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import PaymentInfo
from .serializers import PaymentInfoSerializer

class PaymentsInfoApiView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all payment information",
        responses={200: PaymentInfoSerializer(many=True)}
    )
    def get(self, request):
        # Get the user's payment information
        payments = PaymentInfo.objects.all()[0:20]
        serializer = PaymentInfoSerializer(payments, many=True)
        return Response(serializer.data)
