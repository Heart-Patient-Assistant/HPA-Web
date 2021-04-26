from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SignUpView,
    # EditProfileView,
    PasswordsChangeView,
    PasswordSuccessView,
    ShowProfileView,
    EditProfilePageView,
    CreateProfilePage,
    AboutView,
)
from . import views

app_name = "users"
router = DefaultRouter()
router.register("profile", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("login", views.UserLoginView.as_view()),
    path("upladmedicalrecord", views.UploadMedicalData.as_view()),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("about/", AboutView.as_view(), name="about"),
    # path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(), name="change_password"),
    path("password/password_success/", PasswordSuccessView, name="password_success"),
    path("<int:pk>/profile", ShowProfileView.as_view(), name="show_profile"),
    path(
        "<int:pk>/edit_profile_page",
        EditProfilePageView.as_view(),
        name="edit_profile_page",
    ),
    path(
        "create_profile_page", CreateProfilePage.as_view(), name="create_profile_page"
    ),
]
