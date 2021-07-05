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
    EditDoctorProfile,
    ShowProfilePostsView,
    AppointmentCreateView,
)
from . import views

app_name = "users"
router = DefaultRouter()
router.register("profile", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("upladmedicalrecord", views.UploadMedicalData.as_view()),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("about/", AboutView.as_view(), name="about"),
    # path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(), name="change_password"),
    path("password/password_success/", PasswordSuccessView, name="password_success"),
    path("<int:pk>/profile", ShowProfileView.as_view(), name="show_profile"),
    path(
        "<int:pk>/profile/sensor/",
        include("HPA_Apps.hardware.urls", namespace="hardware"),
    ),
    path(
        "<int:pk>/profile/posts",
        ShowProfilePostsView.as_view(),
        name="show_profile_posts",
    ),
    path(
        "<int:pk>/edit_profile_page",
        EditProfilePageView.as_view(),
        name="edit_profile_page",
    ),
    path(
        "<int:pk>/edit_doctor_page",
        EditDoctorProfile.as_view(),
        name="edit_doctor_page",
    ),
    path(
        "create_profile_page", CreateProfilePage.as_view(), name="create_profile_page"
    ),
    # path(
    #     "<int:pk>/add_speciality", AddDoctorSpeciality.as_view(), name="add_speciality"
    # ),
    path(
        "appointment/create", AppointmentCreateView.as_view(), name="appointment-create"
    ),
    path(
        "<int:pk>/appointment/p/",
        views.AppointmentsForAPatientView.as_view(),
        name="patient-appointments",
    ),
    path(
        "appointment/d/",
        views.AppointmentsForADoctorView.as_view(),
        name="doctor-appointments",
    ),
]
