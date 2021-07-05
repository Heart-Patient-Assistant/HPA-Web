from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers
from HPA_Apps.hardware.models import Sensor


class SensorListSerializer(serializers.HyperlinkedModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Sensor
        fields = [
            "user",
            "SensorType1",
            "HeartRate",
            "SensorType2",
            "SpO2",
            "Time",
        ]

    def get_user(
        self,
        obj,
    ):
        return str(obj.user.email)
