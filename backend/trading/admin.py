from django.contrib import admin
from .models import Instrument, Trade

# Register your models here.
admin.site.register(Instrument)
admin.site.register(Trade)