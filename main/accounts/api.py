from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer,ProfileSerializer
from django.contrib.auth.models import User
from database.models import Profile
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView


# Login API
class LoginController(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    print(request.data)
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

# Get User API
class UserController(generics.ListCreateAPIView):
  serializer_class =ProfileSerializer
  queryset = Profile.objects.all()
  
  def list(self, request):
      queryset = self.get_queryset()
      serializer = ProfileSerializer(queryset, many=True)
      return Response(serializer.data)

class SingleUserController(APIView):
    def get(self, request, pk):
        profile = Profile.objects.all().filter(user_id=pk)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data[0])  


class DeveloperController(APIView):
  serializer_class =ProfileSerializer
  queryset = Profile.objects.all()
  
  def get(self, request):
      profile = Profile.objects.all().filter(role_title="developer")
      serializer = ProfileSerializer(profile, many=True)
      return Response(serializer.data)  
  
     