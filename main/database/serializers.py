from rest_framework import serializers
from .models import  Bug, Role, Comment, Profile
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer



class BugSerializer(serializers.ModelSerializer):
    reported_by = UserSerializer(read_only=True)
    developer_assigned = UserSerializer(read_only=True)

    class Meta:
        model = Bug
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__'
        # to use Bug model comment field in this serializer
        fields = ['id', 'comment_text', 'user', 'created_at', 'updated_at', 'comment_to']


class BugReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        #fields = ['id', 'name', 'created_at']
        fields = '__all__'

