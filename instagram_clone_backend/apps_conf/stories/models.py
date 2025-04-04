from django.utils.timezone import now, timedelta
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from apps_conf.users.models import CustomUser

class Stories(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='stories')
    content = models.FileField(
        upload_to='stories/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'mp4'])],
    )
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        if not self.image and not self.video and not self.caption:
            raise ValidationError("You must choose at least one image,caption or video")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"
    
    @classmethod
    def visible_stories(cls):
        return cls.objects.filter(created_at__gte=now() - timedelta(hours=24))