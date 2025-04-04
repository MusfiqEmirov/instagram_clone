from django.test import TestCase
from apps_conf.users.models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(str(self.user), 'testuser')  # __str__ testi
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_profile_status_default(self):
        self.assertEqual(self.user.profile_status, CustomUser.OPEN_PROFILE)