from .views import PostApiListView,PostApiDetailView,\
    PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView,\
    CommentCreateAPIView,CommentApiListView,CommentDetaliAPIView
from django.urls import path
from . import views
app_name = "blogs_api"
urlpatterns =[
    path('', PostApiListView.as_view()),
    path('posts/<int:pk>/',PostApiDetailView.as_view()),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('posts/<int:pk>/edit/', PostUpdateAPIView.as_view(),name='update',),
    path('posts/<int:pk>/delete/',PostDeleteAPIView.as_view(),name='delete_post'),

    # Comments
    path('comments/', CommentApiListView.as_view(), name='list'),
    path('comments/<int:id>', CommentDetaliAPIView.as_view(), name='Comment_details'),
    path('posts/<int:pk>/createcomments/', CommentCreateAPIView.as_view(), name='create'),


]
