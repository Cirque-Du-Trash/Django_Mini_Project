from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Account
from .models import TransactionHistory

User = get_user_model()

class TransactionHistoryModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123',
            nickname='testnick'
        )
        self.account = Account.objects.create(
            user=self.user,
            account_number='1234567890',
            bank_code='KB',
            account_type='SAVINGS',
            balance=10000
        )
        self.transaction_data = {
            'account': self.account,
            'amount': 5000,
            'balance_after_transaction': 15000,
            'transaction_detail': '급여',
            'transaction_type': 'DEPOSIT',
            'method': 'TRANSFER'
        }

    def test_create_transaction(self):
        # Given: 거래 내역 데이터가 준비되었을 때
        # When: 새로운 거래 내역을 생성하면
        transaction = TransactionHistory.objects.create(**self.transaction_data)

        # Then: 거래 내역이 올바르게 생성되어야 함
        self.assertEqual(transaction.account, self.account)
        self.assertEqual(transaction.amount, self.transaction_data['amount'])
        self.assertEqual(transaction.balance_after_transaction, self.transaction_data['balance_after_transaction'])
        self.assertEqual(transaction.transaction_detail, self.transaction_data['transaction_detail'])
        self.assertEqual(transaction.transaction_type, self.transaction_data['transaction_type'])
        self.assertEqual(transaction.method, self.transaction_data['method'])
        self.assertIsNotNone(transaction.transaction_date)