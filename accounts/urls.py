from django.urls import path
from .views import register, login, verify_email

urlpatterns = [
    path('register/', register, name='user_create'),
    path('login/', login, name='login'),
    path('verify/<str:token>', verify_email, name='verify_email'),
]