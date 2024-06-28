from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='password123', phone='1234567890', country='Testland', first_name='Test', last_name='User')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))
        self.assertEqual(self.user.phone, '1234567890')
        self.assertEqual(self.user.country, 'Testland')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser@example.com')
