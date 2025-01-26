from django.urls import path
from .api import FundsApiView
from rest_framework.routers import DefaultRouter


app_name = 'hedgefunds'


urlpatterns = [
    path('', FundsApiView.as_view(), name='all-funds'),
]
