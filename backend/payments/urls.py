from django.urls import path
from .api import PaymentsInfoApiView


app_name = 'payments'


urlpatterns = [
    path('payments-info/', PaymentsInfoApiView.as_view(), name='payments-info'),
]
