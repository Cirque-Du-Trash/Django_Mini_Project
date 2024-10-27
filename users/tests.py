from django.test import TestCase
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': f'testuser_{uuid.uuid4().hex[:6]}',
            'email': f'test_{uuid.uuid4().hex[:6]}@example.com',
            'password': 'testpassword123',
            'nickname': 'testnick',
            'name': 'Test User',
            'phone_number': '01012345678'
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.nickname, self.user_data['nickname'])
        self.assertEqual(user.name, self.user_data['name'])
        self.assertEqual(user.phone_number, self.user_data['phone_number'])
        self.assertTrue(user.check_password(self.user_data['password']))