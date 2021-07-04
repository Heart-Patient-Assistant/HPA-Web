from django.urls import path 
from . import views
from django.views.generic.base import TemplateView
app_name="services"
urlpatterns =[
path('', TemplateView.as_view(template_name="servicesList.html"),name="servicesList"),
path('getpredictionapi/',views.getPredictionApi,name='getpredictionApi'),
path('getprediction/',views.getPrediction,name="getprediction"),
path('egcapi/',views.egcApi,name='egcApi'),
path('egc/',views.egc,name="egc"),
path('<str:result>', TemplateView.as_view(template_name="get_result.html"),name='getresult'),
]