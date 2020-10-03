from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

# Create your views here.
class UserApiView(APIView):
    serializer_class = UserSerializer


    def get_queryset(self):
        return User.objects.all()

