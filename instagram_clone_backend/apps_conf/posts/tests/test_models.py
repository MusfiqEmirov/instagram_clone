import time
from django.utils import timezone
from datetime import timedelta

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError

from apps_conf.users.models import CustomUser
from apps_conf.posts.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x00\x01\x02\x03',
            content_type='image/jpeg'
        )
        
        self.test_video = SimpleUploadedFile(
            name='test_video.mp4',
            content=b'\x00\x01\x02\x03',
            content_type='video/mp4'
        )

    def test_create_post_with_image(self):
        post = Post.objects.create(
            user=self.user,
            caption='Test caption',
            image=self.test_image
        )
        self.assertEqual(post.caption, 'Test caption')
        self.assertTrue(post.image.name.startswith('post_images/'))
        self.assertEqual(post.like_count, 0)

    def test_create_post_with_video(self):
        post = Post.objects.create(
            user=self.user,
            caption='Video post',
            video=self.test_video
        )
        self.assertEqual(post.caption, 'Video post')
        self.assertTrue(post.video.name.startswith('post_videos/'))

    def test_create_post_with_caption_only(self):
        post = Post.objects.create(
            user=self.user,
            caption='Text only post'
        )
        self.assertEqual(post.caption, 'Text only post')
        self.assertFalse(post.image)  # Fayl yoxdursa `False` qaytarır
        self.assertFalse(post.video)

    def test_post_validation(self):
        post = Post(user=self.user)
        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_post_str_representation(self):
        post = Post.objects.create(
            user=self.user,
            caption='This is a long caption that will be truncated'
        )
        # Modeldəki `__str__`-ə uyğun (nümunə: 20 simvol + ...)
        self.assertEqual(str(post), f"{self.user.username}: This is a long capti...")

    def test_ordering(self):
        # Açıq şəkildə fərqli zamanlar təyin edək
        old_time = timezone.now() - timedelta(minutes=5)
        post1 = Post.objects.create(
            user=self.user,
            caption='First post',
            created_at=old_time  # Açıq şəkildə köhnə zaman
        )
        
        # Bir neçə saniyə gecikdiririk
        time.sleep(1)
        
        # Yeni post üçün cari zaman
        post2 = Post.objects.create(
            user=self.user,
            caption='Second post'
            # created_at avtomatik təyin olunacaq
        )
        
        # Verilənlər bazasını yeniləyək
        posts = list(Post.objects.all())
        
        # Debug məlumatı
        print(f"Post1 created_at: {post1.created_at}")
        print(f"Post2 created_at: {post2.created_at}")
        
        # Əsas yoxlamalar
        self.assertLess(post1.created_at, post2.created_at)  # post1 daha köhnə olmalıdır
        self.assertEqual(posts[0].id, post2.id)  # Yeni post birinci olmalıdır
        self.assertEqual(posts[1].id, post1.id)  # Köhnə post ikinci olmalıdır