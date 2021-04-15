from django.shortcuts import render
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .models import CustomUser


from .forms import MedicalRecordForm
from django.views.generic.edit import CreateView

from . import models,serializers,permissions

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.CustomUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email',)

class CustomUserLoginView(ObtainAuthToken):
    """Creating User authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




class UploadMedicalData(CreateView):
    form_class=MedicalRecordForm
    template_name='post_form.html'
    success_url = '/'
  