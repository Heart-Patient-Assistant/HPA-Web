from django.shortcuts import render
from . import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from HPA_Apps.users.forms import MedicalRecordForm
from .forms import Egc

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render



#cnn
import numpy as np
import pandas as pd
from keras.models import load_model
import wfdb
from numpy import savetxt




 
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

    return render(request,'prediction_form.html',{'form':MedicalRecordForm()})
  
    #

@permission_classes([permissions.AllowAny])
def egc(request):
    response={}
    if request.method=='POST':
        form=Egc(request.POST,request.FILES)
       
        if form.is_valid():
           
            dirpath=os.path.join(dir_path,"cnn")

            '''
            segHeader=os.path.join(dirpath,"seg.hea")
            with open(segHeader, 'wb+') as destination:
                  for chunk in request.FILES['egcheader'].chunks():
                    destination.write(chunk)
            
            segData=os.path.join(dirpath,"seg.data")
            with open(segData, 'wb+') as destination:
                  for chunk in request.FILES['egcheader'].chunks():
                    destination.write(chunk)
           '''
  # set the the file as a record 

            record = wfdb.rdrecord(dirpath+'/seg04',sampfrom=0,sampto=185 ,channels=[2])
            data = record.p_signal


            
            savetxt(dirpath+'/data4.csv',data, delimiter=',', newline=",")

            datapath=os.path.join(dirpath,"data4.csv")
            test = pd.read_csv(datapath, header = None)


            
            model=load_model(dirpath+"/model.h5")
    


            y_pred=model.predict(test)
            categories=["Normal beat", "unknown Beat", "Ventricular ectopic beat", "Supraventricular ectopic beat", "Fusion Beat"]
            categoryIndex=np.argmax(y_pred)
            prediction_cat=categories[categoryIndex]
            print(prediction_cat)
            response["prediction"]=prediction_cat

            return HttpResponseRedirect(
                reverse('services:getresult',
                kwargs={'result':f'{response["prediction"]}'}))

    return render(request,'prediction_form.html',{'form':Egc()})
  

@api_view(['POST','GET'])
@permission_classes([permissions.AllowAny])
def egcApi(request): 
        serializer=serializers.EgcSerializer(data=request.data)
    
        response={}    
        if serializer.is_valid():
                #getiing values out of bject 
            dirpath=os.path.join(dir_path,"cnn")

            '''
            segHeader=os.path.join(dirpath,"seg.hea")
            with open(segHeader, 'wb+') as destination:
                  for chunk in request.FILES['egcheader'].chunks():
                    destination.write(chunk)
            
            segData=os.path.join(dirpath,"seg.data")
            with open(segData, 'wb+') as destination:
                  for chunk in request.FILES['egcheader'].chunks():
                    destination.write(chunk)
           '''
  # set the the file as a record 

            record = wfdb.rdrecord(dirpath+'/seg04',sampfrom=0,sampto=185 ,channels=[2])
            data = record.p_signal


            
            savetxt(dirpath+'/data4.csv',data, delimiter=',', newline=",")

            datapath=os.path.join(dirpath,"data4.csv")
            test = pd.read_csv(datapath, header = None)


            
            model=load_model(dirpath+"/model.h5")
    


            y_pred=model.predict(test)
            categories=["Normal beat", "unknown Beat", "Ventricular ectopic beat", "Supraventricular ectopic beat", "Fusion Beat"]
            categoryIndex=np.argmax(y_pred)
            prediction_cat=categories[categoryIndex]
            print(prediction_cat)

            response['prediction']= prediction_cat
        
        else:
            response['respose']=serializer.errors
            
        return Response(response)
