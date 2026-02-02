from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import login_view

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view()),
    path("login/", login_view),
]