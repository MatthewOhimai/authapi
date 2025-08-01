from rest_framework.views import APIView  # Imported apiview from drf
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# Create your views here.

class RegisterView(APIView):  # Registering new user
    def post(self, request):  # Post requests
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():  # make sure the provided data is valid
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):  # For Logining user
    def post(self, request): # post request
        "get the email and password from the requested data"
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        "checking if user is valid"
        if user:
            "Generates JWT tokens and serializes the user"
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            "returns the jwt token in response"
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=400) # Gives error message upon failed authentication

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):  # GET request
        serializer = UserSerializer(request.user)  # Serializes the authenticated or logged-in user
        return Response(serializer.data)  # returns serialized data 
    
