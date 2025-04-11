from django.test import TestCase
from django.core.exceptions import ValidationError
from apps_conf.users.models import CustomUser
from apps_conf.posts.models import Post
from apps_conf.stories.models import Story
from apps_conf.reactify.models import Like, Comment


class CommentAndLikeModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password123')

        self.post = Post.objects.create(user=self.user, content="Test post content", caption="Test caption")
        self.story = Story.objects.create(user=self.user, caption="Test story caption")
        self.comment = Comment.objects.create(user=self.user, post=self.post, text="Test comment")

    def test_create_post_without_caption_image_or_video(self):
        with self.assertRaises(ValidationError):
            post = Post(user=self.user, content="Test post content")
            post.full_clean()  

    def test_create_valid_post_with_caption(self):
        post = Post(user=self.user, content="Test post with caption", caption="Test caption")
        post.full_clean() 
        post.save()
        self.assertEqual(post.caption, "Test caption")


    def test_create_comment_with_post(self):
        comment = Comment.objects.create(user=self.user, post=self.post, text="This is a comment")
        
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.text, "This is a comment")
        self.assertIsNone(comment.story)
        self.assertIsNotNone(comment.created_at)

    def test_create_comment_with_story(self):
        comment = Comment.objects.create(user=self.user, story=self.story, text="This is another comment")
        
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.story, self.story)
        self.assertEqual(comment.text, "This is another comment")
        self.assertIsNone(comment.post)
        self.assertIsNotNone(comment.created_at)

    def test_create_comment_with_no_post_or_story(self):
        with self.assertRaises(ValidationError):
            comment = Comment.objects.create(user=self.user, text="Invalid comment")
            comment.clean()

    def test_create_like_with_post(self):
        like = Like.objects.create(user=self.user, post=self.post)
        
        self.assertEqual(like.user, self.user)
        self.assertEqual(like.post, self.post)
        self.assertIsNone(like.story)
        self.assertIsNone(like.comment)
        self.assertIsNotNone(like.created_at)

    def test_create_like_with_story(self):
        like = Like.objects.create(user=self.user, story=self.story)
        
        self.assertEqual(like.user, self.user)
        self.assertEqual(like.story, self.story)
        self.assertIsNone(like.post)
        self.assertIsNone(like.comment)
        self.assertIsNotNone(like.created_at)

    def test_create_like_with_comment(self):
        like = Like.objects.create(user=self.user, comment=self.comment)
        
        self.assertEqual(like.user, self.user)
        self.assertEqual(like.comment, self.comment)
        self.assertIsNone(like.post)
        self.assertIsNone(like.story)
        self.assertIsNotNone(like.created_at)

    def test_create_like_with_no_post_story_or_comment(self):
        with self.assertRaises(ValidationError):
            like = Like.objects.create(user=self.user)
            like.clean()


    def test_str_method_with_post(self):
        like = Like.objects.create(user=self.user, post=self.post)
        self.assertEqual(str(like), f"{self.user.username} likes post {self.post}")

    def test_str_method_with_story(self):
        like = Like.objects.create(user=self.user, story=self.story)
        self.assertEqual(str(like), f"{self.user.username} likes story {self.story}")

    def test_str_method_with_comment(self):
        like = Like.objects.create(user=self.user, comment=self.comment)
        self.assertEqual(str(like), f"{self.user.username} likes comment: {self.comment}")
