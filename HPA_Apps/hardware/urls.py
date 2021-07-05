from django.urls import path
from .views import receive_data, SensorReading

app_name = "hardware"

urlpatterns = [
    path("data/", receive_data, name="receive_data"),
    path("reading/", SensorReading.as_view(), name="reading"),
]
