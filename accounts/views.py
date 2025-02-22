from django.contrib.auth import authenticate
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User

# Create your views here.
        
@api_view(['POST'])
def register(request):
    # Get data from request
    username = request.data.get("user_name")
    email = request.data.get("user_email")
    password = request.data.get("user_password")

    # Validate required fields
    if not all([username, email, password]):
        return Response({
            "error": "Username, email and password are required"
        }, status=400)

    # Check if user exists
    if User.objects.filter(email=email).exists():
        return Response({"error": "User already exists"}, status=400)
    
    try:
        # Create user properly using all required fields
        user = User.objects.create_user(  # Use create_user instead of create
            username=username,
            email=email,
            password=password,  # No need to hash manually, create_user does it
            user_status=User.INACTIVE
        )

        # Generate token for verification
        token = Token.objects.create(user=user)
        verification_link = f"http://127.0.0.1:8000/account/verify/{token.key}"

        # Send verification email
        send_mail(
            "Verify Your Email",
            f"Click this link to verify your email: {verification_link}",
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )

        return Response({"message": "Check your email for verification"}, status=201)
    
    except Exception as e:
        return Response({"error": str(e)}, status=400)

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
    email = request.data.get("user_email")
    password = request.data.get("user_password")
    
    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get user by email
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Authenticate with username and password
    # Note: Django's authenticate expects username, but we're using email
    # If you're using AbstractUser, the username field is username, not email
    authenticated_user = authenticate(username=user.username, password=password)
    
    if not authenticated_user:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    if authenticated_user.user_status != User.ACTIVE:
        return Response({"error": "Email not verified"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Generate JWT tokens (access + refresh)
    refresh = RefreshToken.for_user(authenticated_user)

    return Response({
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
    })
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({
        "email": user.email,
        "username": user.username
    })