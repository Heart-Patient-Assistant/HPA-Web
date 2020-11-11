from .views import PostApiListView,PostApiDetailView,PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView
from django.conf.urls import url
from django.urls import path
app_name = "blogs_api"
urlpatterns =[
    path('', PostApiListView.as_view()),
    path('posts/<int:pk>/',PostApiDetailView.as_view()),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('posts/<int:pk>/edit/', PostUpdateAPIView.as_view(),name='update',),
    path('posts/<int:pk>/delete/',PostDeleteAPIView.as_view(),name='delete_post'),


]
