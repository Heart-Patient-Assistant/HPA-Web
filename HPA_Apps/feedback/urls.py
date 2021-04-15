from django.urls import path

from . import views
app_name='feedback'
urlpatterns =[
path('givefeedbackapi/',views.giveFeedbackApi,name='givefeedbackApi'),
path('givefeedback/',views.giveFeedback.as_view(),name='givefeedback')
]
