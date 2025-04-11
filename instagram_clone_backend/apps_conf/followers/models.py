from django.db import models
from django.conf import settings


class Follow(models.Model):
    follower = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name='following',
    on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        ordering = ['-created_at'] # azalan sira ile getirsin deye

    def save(self, *args, **kwargs):
        if self.follower == self.following:
            raise ValueError("istifadeci ozunu izleye bilmez")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
