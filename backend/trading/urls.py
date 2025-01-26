from django.urls import path
from .api import TradesApiView, IntrumentsApiView, TradeApiView

app_name = 'trading'

urlpatterns=[
    path('instruments/', IntrumentsApiView.as_view(), name='instrument-list'),
    path('trades/', TradesApiView.as_view(), name='trade-list'),
    path('trade/', TradeApiView.as_view(), name='trade-create'),
]