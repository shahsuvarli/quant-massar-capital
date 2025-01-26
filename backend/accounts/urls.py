from django.urls import path
from .api import UserProfliesApiView
from rest_framework.routers import DefaultRouter

# Use DRF's router for ViewSets
router = DefaultRouter()
# router.register(r'accounts', AccountApiView, basename='accounts')  # Maps /api/items/

urlpatterns = [
    # Any non-ViewSet-specific URLs can go here
    path('user_profiles/', UserProfliesApiView.as_view(), name='user-profiles'),
]

# Include the router-generated URLs
urlpatterns += router.urls
