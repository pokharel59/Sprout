from django.urls import path
from .views import register, login, verify_email, get_user_info
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", register, name='user_create'),
    path("login/", login, name='login'),
    path("verify/<str:token>", verify_email, name='verify_email'),
    path("user-info/", get_user_info , name="user-info")
]