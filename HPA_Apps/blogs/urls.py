from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CategoryCreateView,
    CategoryView,
    LikeView,
    CommentCreateView,
)

app_name = "blogs"
urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("posts", BlogListView.as_view(), name="posts"),
    path("category/new/", CategoryCreateView.as_view(), name="category_new"),
    path("category/<str:cats>/", CategoryView, name="category"),
    path("like/<int:pk>", LikeView, name="like_post"),
    path("post/<int:pk>/comment/", CommentCreateView.as_view(), name="add_comment"),
]
