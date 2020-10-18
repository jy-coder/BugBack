from .models import Role, Comment, Bug
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from .serializers import BugSerializer,RoleSerializer, CommentSerializer, BugReportSerializer
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








class BugListAPI (generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    queryset = Bug.objects.all()

    ##view lists of bugs
    def list(self, request):
        queryset = self.get_queryset()
        serializer = BugSerializer(queryset, many=True)
        return Response(serializer.data)

    ##create bugs
    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


## need to add single bug view (not completed)
class BugSingleAPI (generics.ListAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BugSerializer(queryset, many=True)
        return Response(serializer.data)



class AddBugReportAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        serializer = BugReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # 201 is created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else return error status 400
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#view and update bug report
class BugReportAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self, id):   # id as the primary key
        try:
            return Bug.objects.get(id=id)

        except Bug.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,id):
        #  get all reports from db
        report = self.get_object(id)
        # parse all reports into JSON object
        serializer = BugReportSerializer(report)
        return Response(serializer.data)

    def patch(self, request, id):
        print("patch req {}".format(request.data))
        instance = self.get_object(id)
        serializer = BugReportSerializer(instance, data=request.data,
                                    partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")




