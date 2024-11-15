from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


def index(request):
	return HttpResponse("Holla")


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_users(request):
	users = User.objects.all()
	serializer = RegisterSerializer(users, many=True)
	return Response(serializer.data, status=status.HTTP_201_CREATED)
