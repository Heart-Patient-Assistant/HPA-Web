from django.urls import path

from . import views
app_name='feedback'
urlpatterns =[
path('givefeedback/',views.giveFeedback,name='givefeedback')
]
