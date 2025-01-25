from django.contrib import admin
from .models import HedgeFundCompany, Fund, Portfolio   

# Register your models here.
admin.site.register(HedgeFundCompany)
admin.site.register(Fund)
admin.site.register(Portfolio)
