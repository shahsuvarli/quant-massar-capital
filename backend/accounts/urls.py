from django.urls import path
from .api import UserView
from rest_framework.routers import DefaultRouter
from .api import CustomTokenObtainPairView, LogoutApiView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


app_name = 'accounts'

urlpatterns = [
    path('', UserView.as_view(), name='user_profiles'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('register/', RegisterView.as_view(), name='register'),
]
