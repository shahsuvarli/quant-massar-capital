from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfilesGetSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class UserProfilesApiView(APIView):
    @swagger_auto_schema(operation_description="Retrieve all accounts", responses={200: UserProfilesGetSerializer(many=True)})
    def get(self, request):
        user_profiles = UserProfile.objects.all()
        serializer = UserProfilesGetSerializer(user_profiles, many=True)
        return Response(serializer.data)
