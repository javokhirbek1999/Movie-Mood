from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response

from api.permissions.user_permissions import IsOwnerOrReadOnly, AllowAny
from api.serializers.user_serializers import UserSerializer, AuthTokenSerializer

class UserAPIView(generics.CreateAPIView):

    """API View for creating user."""
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UpdateDeleteUserAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API View for for retrieving, updating and deleting user."""
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = UserSerializer

    def get_object(self):
        return get_user_model().objects.get(username=self.kwargs.get('pk'))


class AllUsers(generics.ListAPIView):

    """API View for listing all available users."""
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class AuthTokenAPIView(ObtainAuthToken):

    """API View for obtaining authentication token."""
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


    def post(self, request, *args, **kwargs):
        
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })