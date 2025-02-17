from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import User

# Create your views here.
        
@api_view(['POST'])
def register(request):
     user_name = request.data.get("user_name")
     user_email = request.data.get("user_email")
     password = request.data.get("password")

     if User.objects.filter(user_email=user_email).exists():
          return Response({"error": "User already exists"}, status=400)
     
     user = User.objects.create(
          user_name=user_name,
          user_email=user_email,
          user_status=User.INACTIVE
     )

    # Generate token for verification
     token = Token.objects.create(user=user)
     verification_link = f"http://127.0.0.1:8000/api/verify/{token.key}"

    # Send verification email
     send_mail(
          "Verify Your Email",
          f"Click this link to verify your email: {verification_link}",
          settings.DEFAULT_FROM_EMAIL,
          [user_email],
     )

     return Response({"message": "Check your email for verification"}, status=201)

@api_view(["GET"])
def verify_email(request, token):
    try:
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
        user.user_status = User.ACTIVE
        user.save()
        token_obj.delete()
        return Response({"message": "Email verified! You can now log in."})
    except:
        return Response({"error": "Invalid token"}, status=400)
    
@api_view(['POST'])
def login(request):
     user_email = request.data.get("user_email")
     password = request.data.get("password")

     user = get_object_or_404(User, user_email=user_email)

     if user.user_status != User.ACTIVE:
          return Response({"error": "Email not verified"}, status=400)
     
     token, created = Token.objects.get_or_create(user=user)
     return Response({"token": token.key, "user": user_email})
    