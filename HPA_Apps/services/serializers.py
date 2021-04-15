from HPA_Apps.users.models import CustomUser
from rest_framework import serializers

class MLpredictionserializer(serializers.Serializer):
   
    age=serializers.IntegerField()
    sex=serializers.IntegerField()
    cp=serializers.IntegerField()
    trestbps=serializers.IntegerField()
    chol=serializers.IntegerField()
    fbs=serializers.IntegerField()
    restecg=serializers.IntegerField()
    thalach=serializers.IntegerField()
    exang=serializers.IntegerField()
    oldpeak=serializers.IntegerField()
    slope=serializers.IntegerField()
    ca=serializers.IntegerField()
    thal=serializers.IntegerField()
    
   
