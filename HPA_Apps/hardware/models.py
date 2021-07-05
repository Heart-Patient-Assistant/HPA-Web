from django.db import models
from django.db.models.fields import NullBooleanField
from django.utils import timezone
from HPA_Apps.users.models import User

# Create your models here.


class Sensor(models.Model):
    user = models.ForeignKey(User, related_name="Sensor", on_delete=models.CASCADE)
    SensorType1 = models.CharField(max_length=25, null=True, blank=True)
    HeartRate = models.CharField(max_length=5, null=True, blank=True)
    SensorType2 = models.CharField(max_length=25, null=True, blank=True)
    SpO2 = models.CharField(max_length=5, null=True, blank=True)
    Time = models.DateTimeField(default=timezone.now, blank=True)
