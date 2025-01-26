from django.urls import path
from .api import FundsApiView, PortfoliosApiView, HedgeFundCompanyApiView
from rest_framework.routers import DefaultRouter


app_name = 'hedgefunds'


urlpatterns = [
    path('', FundsApiView.as_view(), name='all-funds'),
    path('portfolios/', PortfoliosApiView.as_view(), name='all-portfolios'),
    path('companies/', HedgeFundCompanyApiView.as_view(), name='all-companies'),
]
