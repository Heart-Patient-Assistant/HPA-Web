from django.shortcuts import render
from . import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

# Create your views here.
@api_view(["POST","GET"])
@permission_classes([permissions.AllowAny])
def giveFeedback(request):
    data={}
    serializer=serializers.FeedbackSerializer(data=request.data)
   
    if request.method=="POST":
        if serializer.is_valid():
            serializer.save()
            data["sucess"]="successfully feeded"
        else:
            data['fail']="fail to feed"
        
    else:
        data["rate"]="assign your rate"
        data["feedback_category"]="assign the category"
        data["feedback_message"]="assign the message"
         
        
    return Response(data)
    
