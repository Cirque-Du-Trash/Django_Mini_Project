from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from .serializers import UserRegisterSerializer, UserLoginSerializer, LogoutSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]  # 누구나 접근 가능

class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

class UserLogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            try:
                token_instance = OutstandingToken.objects.get(token=token)
                BlacklistedToken.objects.create(token=token_instance)
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except OutstandingToken.DoesNotExist:
                return Response({'detail': 'Token does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






