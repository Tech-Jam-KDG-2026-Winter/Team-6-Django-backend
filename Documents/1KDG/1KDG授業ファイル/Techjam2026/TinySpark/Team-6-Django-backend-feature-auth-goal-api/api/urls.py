from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_view, create_goal, list_goals

urlpatterns = [
    path("register/", register_view),
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("goals/create/", create_goal),
    path("goals/", list_goals),
]