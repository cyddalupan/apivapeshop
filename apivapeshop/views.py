from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import UserLoginSerializer

class CheckLogin(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		return Response({'is_logged_in': True})


class LoginView(APIView):
  queryset = User.objects.all() 

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')

    print(username)

    user = authenticate(username=username, password=password)

    if user:
      token, _ = Token.objects.get_or_create(user=user)
      return Response({'token': token.key})
    else:
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):

    def post(self, request):
        # Call Django's logout function to clear the user's session
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
