from .models import Role, Comment, Bug
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from .serializers import BugSerializer, CommentSerializer
from accounts.serializers import UserSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.http import HttpResponse, JsonResponse



class BugReportAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        reports = Bug.objects.all().order_by('id','pk')
        serializer = BugSerializer(reports, many=True)
        return Response(serializer.data)

    #http://localhost:8000/bugs
    def post(self, request):
        name = request.data.get('name')
        instance = Bug(reported_by=self.request.user,name=name)

        instance.save()
        
        if(instance):
            return Response(status=status.HTTP_201_CREATED)
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
        report = Bug.objects.filter(id=pk).update(**request.data)
        return Response(status=status.HTTP_200_OK)  





class SearchBugAPI(APIView):
    def get(self, request):
        queryset = Bug.objects.all()
        bugname = self.request.GET.get('q', None).replace(" ", "")
        if bugname is not None:
            queryset = queryset.filter(name__contains=bugname)
            serializer = BugSerializer(queryset,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)




class CommentAPI(APIView):
    def get(self, request, pk):
        comments = Comment.objects.all().filter(bug_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)  

    def post(self, request,pk):
        text= request.data.get('comment_text')
        instance = Comment(user=self.request.user,comment_text=text,bug_id=pk)
        instance.save()
        if(instance):
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


