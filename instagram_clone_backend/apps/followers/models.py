from django.db import models

from users.models import *


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        ordering = ['-created_at'] # azalan sira ile getirsin deye

    def save(self, *args, **kwargs):
        if self.follower == self.following:
            raise ValueError("istifadeci ozunu izleye bilmez")
        super().save(*args, **kwargs)

