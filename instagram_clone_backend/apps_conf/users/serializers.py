from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps_conf.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'profile_picture', 'bio')
