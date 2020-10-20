from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer,ProfileSerializer
from django.contrib.auth.models import User
from database.models import Profile
from django.http import HttpResponse, JsonResponse


##########

# Normal Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)


    user_instance = UserSerializer(User, context=self.get_serializer_context()).data
    
    return Response({
      "user": user_instance,
      "token": AuthToken.objects.create(User)[1]
    })







# Login API
class LoginAPI(generics.GenericAPIView):
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
class UserAPI(generics.ListCreateAPIView):
  # permission_classes = [
  #   permissions.IsAuthenticated,
  # ]
  serializer_class =ProfileSerializer
  queryset = Profile.objects.all()
  
  def list(self, request):
      # Note the use of `get_queryset()` instead of `self.queryset`
      queryset = self.get_queryset()
      serializer = ProfileSerializer(queryset, many=True)
      return Response(serializer.data)

class SingleUserAPI(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer