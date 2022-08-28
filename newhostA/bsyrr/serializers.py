
from rest_framework import serializers
from bsyrr.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        password2 = serializers.CharField(
            style={'input_type': 'password'}, write_only=True)
        model = User
        field = ['email', 'firstname', 'lastname', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                "password and confirm password does'nt match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
