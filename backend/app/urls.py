from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Quantm API",
        default_version="v1",
        description="API documentation for Quantm",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shahsuvarli.elvin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path("api/", include("accounts.urls")),  # Your API URLs
    path('admin/', admin.site.urls),
]
