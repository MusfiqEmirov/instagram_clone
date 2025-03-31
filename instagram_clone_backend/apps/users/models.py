from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True, max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    @property
    def followers_count(self):
        return self.followers.count()
    
    @property
    def following_count(self):
        return self.following.count()
    
    def __str__(self):
        return f"{self.follower} follows {self.following}"