from django.urls import path 
from . import views
app_name='services'
urlpatterns =[
path('getprediction/',views.getPrediction,name='getprediction')
]