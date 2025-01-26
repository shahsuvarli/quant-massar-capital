from django.urls import path
from .api import RiskMetricApiView

app_name = 'risk'


urlpatterns = [
    path('risk-metrics/', RiskMetricApiView.as_view(), name='risk-metrics'),
]
