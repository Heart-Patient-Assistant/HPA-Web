from django.urls import path


#getting token for authenticated user[tutorial]
#https://www.django-rest-framework.org/api-guide/authentication/#apache-mod_wsgi-specific-configuration
from rest_framework.authtoken.views import obtain_auth_token

from . import views


app_name = "users_api"

urlpatterns = [
    path('signup/',views.createaccount,name='createaccount'),
    path('gettoken/',obtain_auth_token,name='gettoken'),
    path('editprofile/',views.editprofile,name='edit')
]