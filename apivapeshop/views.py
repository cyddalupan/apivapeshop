from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .serializers import UserLoginSerializer

class LoginView(APIView):
  queryset = User.objects.all() 
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
      return Response({'is_logged_in': True})

  def post(self, request, *args, **kwargs):
      serializer = UserLoginSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)

      user = authenticate(
          username=serializer.validated_data['username'],
          password=serializer.validated_data['password']
      )

      if user:
          token, created = Token.objects.get_or_create(user=user)
          return Response({'token': token.key})
      else:
          return Response({'error': 'Invalid credentials'}, status=400)
