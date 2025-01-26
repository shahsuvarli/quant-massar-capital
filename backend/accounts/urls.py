from django.urls import path
from .api import UserProfilesApiView
from rest_framework.routers import DefaultRouter

# Use DRF's router for ViewSets
app_name = 'accounts'
# router = DefaultRouter()
# router.register(r'accounts', AccountApiView, basename='accounts')  # Maps /api/items/

urlpatterns = [
    # Any non-ViewSet-specific URLs can go here
    path('', UserProfilesApiView.as_view(), name='user_profiles'),
]



# Include the router-generated URLs
# urlpatterns += router.urls
