# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # , csrf_protect,
from django.views.generic import ListView
import json
from django.shortcuts import get_object_or_404
from HPA_Apps.users.models import Profile

# from django.contrib.auth.decorators import login_required


from .models import Sensor
from HPA_Apps.users.models import User


class SensorReading(ListView):
    model = Sensor
    template_name = "registration/reading.html"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Sensor.objects.filter(user=pk)

    def get_context_data(self, *args, **kwargs):
        context = super(SensorReading, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context

# @login_required
@csrf_exempt
def receive_data(request, pk):
    try:
        print("\n")
        data = json.loads(request.body)
        userId = data.get("user", None)
        type1 = data.get("sensorType1", None)
        heart_rate = data.get("reading", None)
        type2 = data.get("sensorType2", None)
        spo2 = data.get("SpO2", None)

        sensor = Sensor()
        if heart_rate == 0:
            print("hahaha u're dead")
        else:
            print(userId)
            print(type1)
            print(heart_rate)
            print(type2)
            print(spo2)
            patient = User.objects.get(id=userId)
            sensor.user = patient
            sensor.SensorType1 = type1
            sensor.HeartRate = heart_rate
            sensor.SensorType2 = type2
            sensor.SpO2 = spo2
            sensor.save()
        # return get_user(request)
        return HttpResponse("hello")
        # return render(
        #     request,
        #     "reading.html",
        # )

    except:
        return HttpResponse("Sensor isn't connected")
