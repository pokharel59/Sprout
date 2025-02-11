from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, Subject, Content, Activity
from .serializers import UserSerializer, SubjectSerializer, ContentSerializer, ActivitySerializer

# Create your views here.
@api_view(['GET'])
def user_profile(request, user_id=None):
    if user_id:
        user = User.objects.filter(user_id=user_id).first()
        if user:
            serilaizer = UserSerializer(user)
            return Response(serilaizer.data, status=status.HTTP_200_OK)
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def user_info(request):
    serilaizer = UserSerializer(data=request.data)
    if serilaizer.is_valid():
        serilaizer.save()
        return Response(serilaizer.data, status=status.HTTP_201_CREATED)
    return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def subject_request(request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def content_request(request, subject_id=None):
     contents = Content.objects.filter(subject_id=subject_id)
     serializer = ContentSerializer(contents, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def activity_request(request, content_id=None):
     activity = Activity.objects.filter(content_id=content_id)
     serializer = ActivitySerializer(activity, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)
