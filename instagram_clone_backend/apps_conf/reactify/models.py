from django.db import models
from django.core.exceptions import ValidationError

from apps_conf.users.models import CustomUser 
from apps_conf.posts.models import Post 
from apps_conf.stories.models import Story


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=22200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if not self.post and not self.story:
            raise ValidationError("You must choose at least one post or Story")
        
    def __str__(self):
        if self.post:
            return f"{self.user.username} likes post {self.post}"
        return f"{self.user.username} likes Story {self.story}"

        

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_user_post_like'),
            models.UniqueConstraint(fields=['user', 'story'], name='unique_user_story_like'),
            models.UniqueConstraint(fields=['user', 'comment'], name='unique_user_comment_like'),
    ]


    def clean(self):
        if not self.post and not self.story and not self.comment:
            raise ValidationError("You must choose at least one post, story or comment")
        
    def __str__(self):
        if self.post:
            return f"{self.user.username} likes post {self.post}"
        if self.story: 
            return f"{self.user.username} likes story {self.story}"
        return f"{self.user.username} likes comment: {self.comment}"
    

 
