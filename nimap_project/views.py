from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Client, Project
from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def client_list_create(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        client_name = request.data.get('client_name')
        client = Client.objects.create(client_name=client_name, created_by=request.user)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        client.client_name = request.data.get('client_name', client.client_name)
        client.save()
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_project(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    serializer = CreateProjectSerializer(data=request.data)
    
    if serializer.is_valid():
        project = serializer.save(client=client, created_by=request.user)
        project.users.set(serializer.validated_data['users'])
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_projects(request):
    projects = Project.objects.filter(users=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
