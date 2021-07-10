from django.urls import path
from django.views.generic import TemplateView
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
    # ================ Static Pages
    path(
        "recipes/",
        TemplateView.as_view(template_name="Static_Pages/recipes.html"),
        name="recipes",
    ),
    path(
        "recipes-1/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single1.html"),
        name="recipes1",
    ),
    path(
        "recipes-2/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single2.html"),
        name="recipes2",
    ),
    path(
        "recipes-3/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single3.html"),
        name="recipes3",
    ),
    path(
        "recipes-4/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single4.html"),
        name="recipes4",
    ),
    path(
        "recipes-5/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single5.html"),
        name="recipes5",
    ),
    path(
        "recipes-6/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single6.html"),
        name="recipes6",
    ),
    path(
        "recipes-7/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single7.html"),
        name="recipes7",
    ),
    path(
        "recipes-8/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single8.html"),
        name="recipes8",
    ),
    path(
        "recipes-9/",
        TemplateView.as_view(template_name="Static_Pages/recipes-single9.html"),
        name="recipes9",
    ),
    path(
        "activities/",
        TemplateView.as_view(template_name="Static_Pages/activities.html"),
        name="activities",
    ),
]
