from .models import User, Role, Comment, Bug
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, BugSerializer,RoleSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)




class RoleViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Role.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(user)
        return Response(serializer.data)


class BugViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Bug.objects.all()
        serializer = BugSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bug.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BugSerializer(user)
        return Response(serializer.data)