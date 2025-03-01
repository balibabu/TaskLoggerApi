from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'status': 'error', 'message': 'Username taken'}, status=400)
    User.objects.create_user(username=username, password=password)
    return Response({'status': 'success', 'message': 'User registered'}, status=201)

@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    else:
        return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
def signout(request):
    logout(request)
    return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)