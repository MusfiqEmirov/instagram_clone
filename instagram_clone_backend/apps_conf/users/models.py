from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    OPEN_PROFILE = 'Open Profile'
    PRIVATE_PROFILE = 'Private Profile'

    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True, max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    STATUS_LIST = [
        (OPEN_PROFILE,'Open Profile'),
        (PRIVATE_PROFILE,'Private Profile')
        ]
    profile_status = models.CharField(max_length=25, choices=STATUS_LIST, default=OPEN_PROFILE)


    @property
    def followers_count(self):
        return self.followers.count()
    
    @property
    def following_count(self):
        return self.following.count()
    
    def __str__(self):
        return self.username 