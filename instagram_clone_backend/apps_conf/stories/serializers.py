from rest_framework import serializers

from .models import Stories, CustomUser
from .serializers import CustomUserSerializer


class StoriesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Stories
        fields = '__all__' 
    
    def get_image_url(self, object):
        if object.image:
            return object.image.url
        return None
    
    def get_video_url(self, object):
        if object.video:
            return object.video.url
        return None
