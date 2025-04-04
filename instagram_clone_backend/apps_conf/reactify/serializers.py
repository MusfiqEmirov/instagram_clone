from rest_framework import serializers

from .models import Comment, Like
from users.serializers import CustomUserSerializer


class LikeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)


    class Meta:
        model = Like
        fileds = "__all__"


class CommetSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "_all__"