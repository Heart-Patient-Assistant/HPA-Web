from django.shortcuts import render
from . import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from HPA_Apps.users.forms import MedicalRecordForm

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render




 
import pickle
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create your views here.
@api_view(['POST','GET'])
@permission_classes([permissions.AllowAny])
def getPredictionApi(request):     
    #unpacking
    serializer=serializers.MLpredictionserializer(data=request.data)
    response={}
  
    if serializer.is_valid():
        #getiing values out of bject 
        array=list(serializer.data.values())
  
        #loading model https://www.kaggle.com/prmohanty/python-how-to-save-and-load-ml-models
        filepath=os.path.join(dir_path,"model.sav")
        with open(filepath, 'rb') as file:  
            logmodel= pickle.load(file)


        #predicting 
        prediction=logmodel.predict([array])
        
        response['prediction']= "don't worry" if prediction==0 else "we got your back, we reccommed to contact one of our doctors "
        response['worry']=f'{(logmodel.predict_proba([array])[0][1])*100:.2f}%'          
    
    else:
        response['respose']=serializer.errors
        
    return Response(response)

######################################################
@permission_classes([permissions.AllowAny])
def getPrediction(request):
    if request.method=='POST':
        form=MedicalRecordForm(request.POST)
        if form.is_valid():
            array=(list(form.cleaned_data.values()))
        
            filepath=os.path.join(dir_path,"model.sav")
            with open(filepath, 'rb') as file:  
                logmodel= pickle.load(file)
            
            #predicting 
            prediction=logmodel.predict([array])

            response={}
            response['prediction']= "don't worry" if prediction==0 else "we got your back, we reccommed to contact one of our doctors "
            
            response['worry']=f'{(logmodel.predict_proba([array])[0][1])*100:.2f}%'
            
            
            return HttpResponseRedirect(
                reverse('services:getresult',
                kwargs={'result':f'{response["prediction"]} -- {response["worry"] }'}))

    return render(request,'post_form.html',{'form':MedicalRecordForm()})
  
    #