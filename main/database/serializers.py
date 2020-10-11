from rest_framework import serializers
from .models import  Bug, Role, Comment
from django.contrib.auth import authenticate



class BugSerializer(serializers.ModelSerializer):
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

