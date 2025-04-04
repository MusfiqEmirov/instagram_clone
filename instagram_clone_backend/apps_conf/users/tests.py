# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from users.models import CustomUser

# class CustomUserModelTest(TestCase):
#     def setUp(self):
#         """Testlərdən əvvəl istifadəçi yaradırıq"""
#         self.user1 = CustomUser.objects.create_user(
#             username='user1',
#             email='user1@example.com',
#             password='password123',
#             bio='Bio of user1',
#         )
#         self.user2 = CustomUser.objects.create_user(
#             username='user2',
#             email='user2@example.com',
#             password='password123',
#             bio='Bio of user2',
#         )

#     def test_user_creation(self):
#         """İstifadəçi uğurla yaradılmalıdır"""
#         self.assertEqual(self.user1.username, 'user1')  # Username doğru olmalıdır
#         self.assertEqual(self.user2.email, 'user2@example.com')  # Email doğru olmalıdır
#         self.assertTrue(self.user1.check_password('password123'))  # Şifrə doğru olmalıdır

#     def test_followers_count(self):
#         """İstifadəçinin izləyicilərinin sayı doğru olmalıdır"""
#         self.assertEqual(self.user1.followers_count, 0)  # İlk başda izləyici olmalıdır

#         # İstifadəçi 2, istifadəçi 1-i izləyir
#         self.user1.followers.add(self.user2)
#         self.assertEqual(self.user1.followers_count, 1)  # user1-in izləyicilərinin sayı 1 olmalıdır
#         self.assertEqual(self.user2.following_count, 1)  # user2-nin izlədiyi istifadəçi sayı 1 olmalıdır

#     def test_following_count(self):
#         """İstifadəçinin izlədiyi insanların sayı doğru olmalıdır"""
#         self.assertEqual(self.user2.following_count, 0)  # İlk başda heç kim izlənilmir

#         # İstifadəçi 1, istifadəçi 2-ni izləyir
#         self.user2.following.add(self.user1)
#         self.assertEqual(self.user2.following_count, 1)  # user2-nin izlədiyi sayı 1 olmalıdır
#         self.assertEqual(self.user1.followers_count, 1)  # user1-in izləyicilərinin sayı 1 olmalıdır

#     def test_str_method(self):
#         """__str__ metodu doğru işləməlidir"""
#         self.assertEqual(str(self.user1), 'user1')  # user1-in __str__ metodu 'user1' olmalıdır

#     def test_invalid_user_creation(self):
#         """Yanlış məlumatla istifadəçi yaradılması test olunmalıdır"""
#         with self.assertRaises(ValueError):
#             CustomUser.objects.create_user(
#                 username='user3', 
#                 email='',  # Yanlış email
#                 password='password123'
#             )

#     def test_user_profile_picture_upload(self):
#         """İstifadəçinin profil şəkli uğurla yüklənməlidir"""
#         image = SimpleUploadedFile("profile.jpg", b"file_content", content_type="image/jpeg")
#         user_with_picture = CustomUser.objects.create_user(
#             email="user_with_picture@example.com",
#             password="password123",
#             profile_picture=image
#         )
#         self.assertTrue(user_with_picture.profile_picture.name.endswith('profile.jpg'))
