from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserListSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserRegistration(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Account is created', status=201)
    

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def get(self, request):
        pass

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        
        response_data = {
            'token': token.key,
            'username': user.username,
            'id': user.id
        }
        return Response(response_data)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Успешно вышли с аккаунта')
    