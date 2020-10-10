from .models import User, Role, Comment, Bug
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, BugSerializer,RoleSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)




class RoleViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = Role.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    #POST http://127.0.0.1:8000/roles/
    def post(self, request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def get_object(self, pk):
        return Role.objects.get(pk=pk)
    
    #PATCH http://127.0.0.1:8000/roles/2/
    def patch(self, request, pk):
        print("patch req {}".format(request.data))
        instance = self.get_object(pk)
        serializer = RoleSerializer(instance, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")

    #DELETE http://127.0.0.1:8000/roles/2
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BugViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Bug.objects.all()
        serializer = BugSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = Bug.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BugSerializer(user)
        return JsonResponse(serializer.data, safe=False)