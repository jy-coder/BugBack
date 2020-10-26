from .models import Role, Comment, Bug
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from .serializers import BugSerializer,RoleSerializer, CommentSerializer
from accounts.serializers import UserSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.http import HttpResponse, JsonResponse



#########THIS IS FOR TESTING ENDPOINT (can delete ltr)#########3
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



class BugReportAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        #  get all reports from db
        reports = Bug.objects.all()
        # parse all reports into JSON object
        serializer = BugSerializer(reports, many=True)
        return Response(serializer.data)

    #http://localhost:8000/bugs
    def post(self, request):
        name = request.data.get('name')
        instance = Bug(reported_by=self.request.user,name=name)

        instance.save()
        
        if(instance):
            return Response(status=status.HTTP_201_CREATED)
        # else return error status 400
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


class SingleBugAPI(APIView):
    def get(self, request, pk):
        reports = Bug.objects.all().filter(id=pk)
        serializer = BugSerializer(reports, many=True)
        return Response(serializer.data)  


    #http://127.0.0.1:8000/bug/9/
    def delete(self, request, pk, format=None):
        instance = Bug.objects.all().filter(id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #http://127.0.0.1:8000/bug/10/
    def patch(self, request,pk):
        print(request.data)
        report = Bug.objects.filter(id=pk).update(**request.data)
        return Response(status=status.HTTP_200_OK)  








