from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.models import User
from api.serializers import UserSerializer

class LoginUserAPIView(APIView):
    model = User
    def post(self, request, format=None):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({"token": token.key, "created": created, "userProfile": serializer.data}, status=status.HTTP_200_OK)

class RegisterUserAPIView(APIView):
    model = User
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(User, username=serializer.data['username'])
            user.set_password(serializer.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response(
                {"token": token.key, 
                 "loggedUser": serializer.data}, 
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)