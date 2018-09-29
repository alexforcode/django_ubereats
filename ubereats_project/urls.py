"""ubereats_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from ubereats_app.views import index, restaurant_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('restaurant/', restaurant_home, name='restaurant_home'),
    path('restaurant/sign-in/',
         auth_views.LoginView.as_view(template_name='restaurant/sign-in.html'),
         name='restaurant-sign-in'),
    path('restaurant/sign-out/',
         auth_views.LogoutView.as_view(next_page='/'),
         name='restaurant-sign-out'),
]
