"""HPA_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from . import views
from django.contrib import admin
from django.urls import path, include  # new
from django.views.generic.base import TemplateView

# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# Swagger Configuration
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.HPA.com/policies/terms/",
        contact=openapi.Contact(email="contact@HPA.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_urlpatterns = [
    path("users/", include("HPA_Apps.users.api.urls", namespace="users_api")),
    path("blog/", include("HPA_Apps.blogs.api.urls", namespace="blogs_api")),
    path("users/", include("HPA_Apps.hardware.api.urls", namespace="hardware_api")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include("HPA_Apps.users.urls", namespace="users")),
    path("services/", include("HPA_Apps.services.urls")),
    path("blogs/", include("HPA_Apps.blogs.urls", namespace="blogs")),
    path("api/", include(api_urlpatterns)),
    path("feedback/", include("HPA_Apps.feedback.urls", namespace="feedback")),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # enable browsering pics
