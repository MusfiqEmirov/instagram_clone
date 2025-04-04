from rest_framework import serializers

from .models import Post, CustomUser
from users.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__' 
    
    def get_image_url(self, object):
        if object.image:
            return object.image.url
        return None
    
    def get_video_url(self, object):
        if object.video:
            return object.video.url
        return None
