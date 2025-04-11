from rest_framework import serializers

from .models import Follow
from apps_conf.users.serializers import CustomUserSerializer


class FollowSerializer(serializers.ModelSerializer):
    follower = CustomUserSerializer(read_only=True)  # Follower ucun istifadeci melumatlari
    following = CustomUserSerializer(read_only=True)  # Following ucun istifadeci melumatlari

    class Meta:
        model = Follow
        fields = "__all__"

    def validate(self, data):
        if data['follower'] == data['following']:
            raise serializers.ValidationError("istifadeci ozunu izleye bilmez")
        return data


