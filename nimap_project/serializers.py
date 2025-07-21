from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ['id', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()  
    client = serializers.StringRelatedField() 
    
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']

class CreateProjectSerializer(serializers.ModelSerializer):
    users = serializers.ListField(child=serializers.DictField())

    class Meta:
        model = Project
        fields = ['project_name', 'users']

    def validate_users(self, value):
        user_ids = []
        for user in value:
            try:
                user_obj = User.objects.get(id=user['id'])
                user_ids.append(user_obj)
            except User.DoesNotExist:
                raise serializers.ValidationError(f"User with id {user['id']} does not exist.")
        return user_ids

    def create(self, validated_data):
        users = validated_data.pop('users')
        project = Project.objects.create(**validated_data)
        project.users.set(users)
        return project
