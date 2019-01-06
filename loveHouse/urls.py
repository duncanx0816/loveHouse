"""loveList URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, reverse


def index(request):
    return HttpResponseRedirect(reverse('login'))


urlpatterns = [
    path('/', index),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_change/',
         views.PasswordChangeView.as_view(
             template_name='password_change.html',
             success_url='/login'),
         name='password_change'),
    path('wish/', include('wish.urls', namespace='wish')),
    path('note/', include('note.urls', namespace='note')),
    path('memory/', include('memory.urls', namespace='memory')),
]
