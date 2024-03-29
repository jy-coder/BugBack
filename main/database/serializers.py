from rest_framework import serializers
from .models import  Bug,  Comment, Profile, BugUserLikes
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer


class BugSerializer(serializers.ModelSerializer):
    reported_by = UserSerializer()
    developer_assigned = UserSerializer()
    class Meta:
        model = Bug
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class BugUserLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugUserLikes()
        fields = '__all__'
