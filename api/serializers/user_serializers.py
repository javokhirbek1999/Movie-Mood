from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):

    """Serializer for User model."""

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'date_updated', 'password', 'is_staff', 'is_active')
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'date_updated': {'read_only': True},
            'password': {'write_only': True, 'style': {'input_type':'password'}},
        }
    

    def create(self, validated_data):
        return super().create(validated_data)


class AuthTokenSerializer(serializers.Serializer):

    """Serializer for creating authentication token."""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )


        if not user:
            message = _('Validation Error, invalid credentials')
            raise serializers.ValidationError(message, code='authentication')

        if not user.is_active:
            message = _('User is blocked, please contact admin')
            raise serializers.ValidationError(message)

        attrs['user'] = user

        return attrs