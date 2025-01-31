from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# Create your views here.
class UserView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all accounts", responses={200: UserSerializer(many=True)})
    def get(self, request):
        users = User.objects.all()[0:20]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(operation_description="Login to get access token", responses={200: "Access token and refresh token"})
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # response.data.update({
        #     "id": response.data["id"],
        #     "username": response.data["username"],
        #     # "email": response.data["email"],
        #     "phone_number": response.data["phone_number"],
        #     "is_trader": response.data["is_trader"],
        #     "is_investor": response.data["is_investor"],
        #     "account_balance": response.data["account_balance"],
        #     "risk_tolerance": response.data["risk_tolerance"],
        # })
        return response


class LogoutApiView(APIView):

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_description="Logout to invalidate the access token", responses={200: "Logout successful"})
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Logout failed"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    @swagger_auto_schema(operation_description="Register a new user", request_body=RegisterSerializer, responses={201: "User registered successfully!"})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save user to DB
            return Response(
                {"message": "User registered successfully!", "user": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
