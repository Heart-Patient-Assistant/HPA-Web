from django.urls import path
from django.conf.urls import url
from django.urls import path
from .views import BlogCreateView
urlpatterns =[
path('create/', BlogCreateView.as_view(), name='post_new'),



]
