from django.shortcuts import render
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import ObtainAuthToken
from rest_framework.settings import api_settings

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
