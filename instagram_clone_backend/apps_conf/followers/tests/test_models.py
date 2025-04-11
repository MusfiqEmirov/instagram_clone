import time
from django.test import TestCase
from django.contrib.auth import get_user_model

from apps_conf.users.models import CustomUser
from apps_conf.users.serializers import CustomUserSerializer
from apps_conf.followers.models import Follow
from apps_conf.followers.serializers import FollowSerializer

User = get_user_model()

class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='testpass123'
        )

    def test_create_follow_relationship(self):
        """Test creating a follow relationship between users"""
        follow = Follow.objects.create(
            follower=self.user1,
            following=self.user2
        )
        
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.following, self.user2)
        self.assertIsNotNone(follow.created_at)
        
        self.assertEqual(str(follow), "user1 follows user2")

    def test_unique_together_constraint(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, following=self.user2)

    def test_self_follow_prevention(self):
        with self.assertRaises(ValueError):
            Follow.objects.create(follower=self.user1, following=self.user1)

    def test_ordering(self):
        follow1 = Follow.objects.create(follower=self.user1, following=self.user2)
        
        time.sleep(0.1)
        
        follow2 = Follow.objects.create(follower=self.user2, following=self.user1)
        
        follows = Follow.objects.all()
        
        self.assertEqual(follows[0], follow2)
        self.assertEqual(follows[1], follow1)

    def test_related_names(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        
        self.assertEqual(self.user1.following.count(), 1)
        self.assertEqual(self.user1.following.first().following, self.user2)
        
        self.assertEqual(self.user2.followers.count(), 1)
        self.assertEqual(self.user2.followers.first().follower, self.user1)