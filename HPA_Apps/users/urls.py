from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "users"
router = DefaultRouter()
router.register('profile',views.CustomUserViewSet)

urlpatterns =[
    path('',include(router.urls)),
    path('login',views.CustomUserLoginView.as_view()),
]
