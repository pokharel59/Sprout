from django.urls import path
from .views import user_profile, user_info, subject_request, content_request, activity_request

urlpatterns = [
    path('users/<int:user_id>/', user_profile, name='user_request'),
    path('users/', user_info, name='user_create'),
    path('subjects/', subject_request, name='subject_request'),
    path('contents/<int:subject_id>/', content_request, name='content_request'),
    path('activities/<int:content_id>/', activity_request, name='activity_request')
]