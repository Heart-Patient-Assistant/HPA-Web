"""HPA_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView
from django.conf.urls import url


api_urlpatterns = [
    path('users/',include("HPA_Apps.users.api.urls",namespace="users_api")),
    path('blog/',include("HPA_Apps.blogs.api.urls",namespace="blogs_api")),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('users/',include("HPA_Apps.users.urls",namespace="users")),
    path('services/',include("HPA_Apps.services.urls")),
    path('blogs/',include("HPA_Apps.blogs.urls",namespace="blogs")),
    path('api/',include(api_urlpatterns)),

]
