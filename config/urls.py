"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from .views import TodayStatusView, ReportProgressView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', TodayStatusView.as_view(), name='today-status'),
   
    path('api/report/', ReportProgressView.as_view(), name='report-progress'),

]
from . import views 


path('api/status/', views.TodayStatusView.as_view(), name='today-status'),
path('api/report/', views.ReportProgressView.as_view(), name='report-progress'),

urlpatterns = [
    path('api/signup/', views.SignupView.as_view(), name='signup'),
    path('api/login/', views.LoginView.as_view(), name='login'),
]