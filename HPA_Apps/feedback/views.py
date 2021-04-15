from django.shortcuts import render
from . import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from django.views.generic.edit import CreateView
from HPA_Apps.users.models import Feedback
from .forms import FeedBackForm


# Create your views here.
#giving feedback api

@api_view(["POST","GET"])
@permission_classes([permissions.AllowAny])
def giveFeedbackApi(request):
    data={}
    serializer=serializers.FeedbackSerializer(data=request.data)
   
    if request.method=="POST":
        if serializer.is_valid():
            serializer.save()
            data["sucess"]="successfully fed"
        else:
            data['fail']="fail to feed"
        
    else:
        data["rate"]="assign your rate"
        data["feedback_category"]="assign the category"
        data["feedback_message"]="assign the message"
         
        
    return Response(data)
    

#giving feedback 
class giveFeedback(CreateView):
    form_class=FeedBackForm
    template_name='post_form.html'
    success_url = '/'
  