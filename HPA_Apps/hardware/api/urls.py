from django.urls import path

from .views import PostApiListView

app_name = "hardware_api"

urlpatterns = [path("sensor/", PostApiListView.as_view(), name="sensor")]
