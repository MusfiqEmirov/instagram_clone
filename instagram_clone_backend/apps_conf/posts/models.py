from django.db import models
from django.core.exceptions import ValidationError
from apps_conf.users.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(default="No content available") 
    caption = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    video = models.FileField(upload_to='post_videos/', null=True, blank=True)
    like_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # siralamani en yeniyegore edir

    def clean(self):
        caption = self.caption.strip() if self.caption else ''
        if not self.image and not self.video and not caption:
            raise ValidationError("You must choose at least one image,caption or video")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}: {self.caption[:20]}...'