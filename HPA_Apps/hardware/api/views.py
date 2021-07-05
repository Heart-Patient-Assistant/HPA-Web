from rest_framework import generics

from .serializers import SensorListSerializer
from ..models import Sensor

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.permissions import AllowAny
from django.db.models import Q


class PostApiListView(generics.ListCreateAPIView):
    serializer_class = SensorListSerializer
    search_fields = [
        "user__first_name",
        "SensorType1",
        "HeartRate",
        "SensorType2",
        "SpO2",
    ]
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Sensor.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(user__first_name__icontains=query)
                | Q(user__last_name__icontains=query)
                | Q(SensorType1__icontains=query)
                | Q(HeartRate__icontains=query)
                | Q(SensorType2__icontains=query)
                | Q(SpO2__icontains=query)
                | Q(Time__icontains=query)
            ).distinct()
        return queryset_list
