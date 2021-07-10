# from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request

# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import (
    EditProfileForm,
    SignUpForm,
    PasswordsChangeForm,
    ProfilePageForm,
    DoctorPageForm,
    AppointmentForm,
)
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView, ListView
from .models import Doctor, Profile, User, appointment
from HPA_Apps.blogs.models import Post
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import User


from .forms import MedicalRecordForm

# from django.views.generic.edit import CreateView

from . import models, serializers, permissions

# Create your views here.


class CreateProfilePage(CreateView):
    model = Profile
    template_name = "registration/create_user_profile.html"
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    form_class = EditProfileForm
    # fields = ['bio','profile_pic','website_url']
    # success_url = reverse_lazy("home")

    # def get_object(self):
    #     return self.request.user

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("users:show_profile", kwargs={"pk": pk})

    def get_initial(self):
        initial = super().get_initial()
        initial["first_name"] = self.request.user.first_name
        initial["last_name"] = self.request.user.last_name
        initial["email"] = self.request.user.email
        return initial


class EditDoctorProfile(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_doctor_page.html"
    form_class = DoctorPageForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("users:show_profile", kwargs={"pk": pk})


class ShowProfileView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class ShowProfilePostsView(ListView):
    model = Post
    template_name = "registration/user_profile_posts.html"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Post.objects.filter(author=pk)

    # def get(self, request, pk, *args, **kwargs):
    #
    #     # print(pk)
    #     # return Post.objects.filter(pk= Post.author.id())
    #     #  return Post.objects.filter(Post.id == pk)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy("users:password_success")
    template_name = "registration/change_password.html"


def PasswordSuccessView(request):
    return render(request, "registration/password_success.html", {})


# def AboutView(request):
#     return render(request, "registration/about.html", {})


class AboutView(ListView):
    model = Doctor
    template_name = "registration/about.html"
    ordering = ["-id"]

    # def get_context_data(self, *args, **kwargs):
    #     doctors_menu = Doctor.objects.all()
    #     context = super(AboutView, self).get_context_data(*args, **kwargs)
    #     context["doctors_menu"] = doctors_menu
    #     return context


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


# class EditProfileView(generic.UpdateView):
#     form_class = EditProfileForm
#     template_name = "registration/edit_profile.html"

#     def get_success_url(self):
#         pk = self.kwargs["pk"]
#         return reverse("users:show_profile", kwargs={"pk": pk})

#     def get_object(self):
#         return self.request.user


# ----------------------------------------
class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("email",)


class UserLoginView(ObtainAuthToken):
    """Creating User authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UploadMedicalData(CreateView):
    form_class = MedicalRecordForm
    template_name = "post_form.html"
    success_url = "/"


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = appointment
    form_class = AppointmentForm
    template_name = "appointment_create.html"
    # success_url = reverse_lazy("AppointmentCreateView")

    def get_initial(self):
        initial = super().get_initial()
        initial["patient"] = self.request.user
        # initial["doctor"] = User.objects.get(pk=self.kwargs["pk"])
        return initial

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment done successfully")
            return redirect("/users/appointment/create")


class AppointmentsForAPatientView(LoginRequiredMixin, ListView):
    login_url = "/users/login/"
    # redirect_field_name = 'login'
    template_name = "appointment_list.html"

    def get_queryset(self):
        return appointment.objects.filter(patient=self.request.user)


class AppointmentsForADoctorView(LoginRequiredMixin, ListView):
    login_url = "/users/login/"
    redirect_field_name = "account:login"
    template_name = "appointment_list.html"

    def get_queryset(self):
        return appointment.objects.filter(doctor=self.request.user)
