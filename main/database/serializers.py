from rest_framework import serializers
from .models import  Bug, Role, Comment, Profile
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer



class BugSerializer(serializers.ModelSerializer):
    reported_by = UserSerializer()
    developer_assigned = UserSerializer()
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
        fields = '__all__'


