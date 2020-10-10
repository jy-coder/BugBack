from rest_framework import serializers
from .models import User, Bug, Role, Comment
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



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


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")