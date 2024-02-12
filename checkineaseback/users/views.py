from django.shortcuts import render
from rest_framework import generics,views
from .models import UserModel
from .serializer import UserSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class UsersView(generics.ListCreateAPIView):
  queryset = UserModel.objects.all()
  serializer_class= UserSerializer

class UsersUpdateDeleate(generics.RetrieveUpdateDestroyAPIView):
  queryset = UserModel.objects.all()
  serializer_class= UserSerializer

class LoginView(views.APIView):
  def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        serializer = UserLoginSerializer(data={'email': email, 'password': password})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
