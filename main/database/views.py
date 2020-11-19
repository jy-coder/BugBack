from .models import Comment, Bug,BugUserLikes
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from .serializers import BugSerializer, CommentSerializer,BugUserLikesSerializer
from accounts.serializers import UserSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta


class BugsController(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    #http://localhost:8000/bugs
    def get(self, request):
        reports = Bug.objects.all().order_by('-created_at')
        serializer = BugSerializer(reports, many=True)
        return Response(serializer.data)

    #http://localhost:8000/bugs
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        instance = Bug(reported_by=self.request.user,name=name,pk=None,description=description)

        instance.save()
        
        if(instance):
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


class BugController(APIView):
    #http://127.0.0.1:8000/bug/2
    def get(self, request, pk):
        print(self.request.user.id)
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




#http://127.0.0.1:8000/bug/search/?q=bug10
class SearchKeywordController(APIView):
    def get(self, request):
        queryset = Bug.objects.all()
        bugname = self.request.GET.get('q', None)
        if(bugname):
            bugname=bugname.replace(" ", "")
        if bugname is not None:
            queryset = queryset.filter(name__contains=bugname)
            serializer = BugSerializer(queryset,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


## this should work but let me test it ##

class CommentController(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    #http://localhost:8000/comment/2
    def get(self, request, pk):
        comments = Comment.objects.all().filter(bug_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)  

    #http://localhost:8000/comment/3/
    def post(self, request,pk):
        text= request.data.get('comment_text')
        instance = Comment(user=self.request.user,comment_text=text,bug_id=pk)
        instance.save()
        if(instance):
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#http://127.0.0.1:8000/buglikes/20/?type=up 
class BugStatusController(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def get(self, request, pk):
        user_id = self.request.user.id
        bug_likes = BugUserLikes.objects.all().filter(bug_id=pk,user_id=self.request.user.id)
        serializer = BugUserLikesSerializer(bug_likes, many=True)

        return Response(serializer.data)  

    def post(self, request,pk):
        type_ = self.request.GET.get('type', None)
        instance = BugUserLikes(bug_id=pk, user_id=self.request.user.id)
        bug = Bug.objects.filter(id=pk).first()
        if(type_ == "down"):
            bug.upvote_count -= 1
        elif(type_ == "up"):
            bug.upvote_count += 1

        bug.save()
        instance.save()

        return Response(status=status.HTTP_200_OK)

#http://127.0.0.1:8000/bug/assign_search?q=user1
class SearchAssigneeController(APIView):
    def get(self, request):
        queryset = User.objects.all()
        name= self.request.GET.get('q', None)

        if name is not None:
            queryset = queryset.filter(username__startswith=name,username__endswith=name)[0].id

        bug = Bug.objects.filter(reported_by__id=queryset)
        serializer = BugSerializer(bug, many=True)
        return Response(serializer.data)


class SearchTitleController(APIView):
    def get(self, request):
        queryset = Bug.objects.all()
        bugname = self.request.GET.get('q', None)
        if bugname is not None:
            queryset = queryset.filter(name=bugname)
            serializer = BugSerializer(queryset,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


class ViewWeeklyBugController(APIView):
    def get(self, request):
        last_week= datetime.today() - timedelta(days=7)
        count = Bug.objects.filter(created_at__gte=last_week, status="closed").count()
        return Response({"count":count})


class ViewMonthlyBugController(APIView):
    def get(self, request):
        last_month = datetime.today() - timedelta(days=30)
        count = Bug.objects.filter(created_at__gte=last_month, status="closed").count()
        return Response({"count":count})
