from django.urls import path
from .api import TradesApiView, intrumentsApiView

app_name = 'trading'

urlpatterns=[
    path('instruments/', intrumentsApiView.as_view(), name='instrument-list'),
    path('trades/', TradesApiView.as_view(), name='trade-list'),
]