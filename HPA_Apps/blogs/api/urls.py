from . import views
from .views import (
    PostApiListView,
    PostApiDetailView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    postlist,
)

from django.conf.urls import url
from django.urls import path


app_name = "blogs_api"
urlpatterns = [
    path("", PostApiListView.as_view()),
    path("posts/<int:pk>/", postlist.as_view()),
    path("create/", PostCreateAPIView.as_view(), name="create"),
    path(
        "posts/<int:pk>/edit/",
        PostUpdateAPIView.as_view(),
        name="update",
    ),
    path("posts/<int:pk>/delete/", PostDeleteAPIView.as_view(), name="delete_post"),
    url(
        r"posts/(?P<pk>\d+)/comments/$",
        view=views.PostApiDetailView.as_view({"get": "comments", "post": "comments"}),
    ),
    url(
        r"posts/(?P<pk>\d+)/comments/(?P<comment>\d+)/$",
        view=views.PostApiDetailView.as_view({"delete": "remove_comment"}),
    ),
]
