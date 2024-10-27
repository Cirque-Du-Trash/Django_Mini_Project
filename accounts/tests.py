from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Account

User = get_user_model()

class AccountModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123',
            nickname='testnick'
        )
        self.account_data = {
            'user': self.user,
            'account_number': '1234567890',
            'bank_code': 'KB',
            'account_type': 'SAVINGS',
            'balance': 10000
        }

    def test_create_account(self):
        # Given: 계좌 데이터가 준비되었을 때
        # When: 새로운 계좌를 생성하면
        account = Account.objects.create(**self.account_data)

        # Then: 계좌가 올바르게 생성되어야 함
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.account_number, self.account_data['account_number'])
        self.assertEqual(account.bank_code, self.account_data['bank_code'])
        self.assertEqual(account.account_type, self.account_data['account_type'])
        self.assertEqual(account.balance, self.account_data['balance'])