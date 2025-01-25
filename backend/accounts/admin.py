from django.contrib import admin
from .models import User, UserProfile, ApiToken, UserActivity

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(ApiToken)
admin.site.register(UserActivity)