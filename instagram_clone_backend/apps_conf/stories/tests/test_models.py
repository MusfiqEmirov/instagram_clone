from django.test import TestCase
from django.utils.timezone import now, timedelta

from apps_conf.stories.models import Story
from apps_conf.users.models import CustomUser


class StoryModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='storyuser', password='password123')

    def test_create_story_with_caption(self):
        story = Story.objects.create(
            user=self.user,
            caption='A very long caption that exceeds twenty characters',
        )
        self.assertEqual(story.image, None)
        self.assertEqual(story.video, None)

    def test_create_story_with_image(self):
        story = Story.objects.create(
            user=self.user,
            caption='A caption with an image',
            image='story_images/some_image.jpg', 
        )
        self.assertIsNotNone(story.image)
        self.assertEqual(story.video, None)

    def test_create_story_with_video(self):
        story = Story.objects.create(
            user=self.user,
            caption='A caption with a video',
            video='story_videos/some_video.mp4', 
        )
        self.assertEqual(story.image, None)
        self.assertIsNotNone
