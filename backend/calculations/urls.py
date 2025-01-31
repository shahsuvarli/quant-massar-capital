from django.urls import path
from .api import value_at_risk, optimize_portfolio

app_name = 'calculations'


urlpatterns = [
    path('value-at-risk/', value_at_risk,
         name='value-at-risk'),
    path('optimize-portfolio/', optimize_portfolio, name='optimize-portfolio'),
]
