from django.test import TestCase
from accounts.models import CustomUser, Account, TransactionHistory

class CustomUserModelTest(TestCase):
    def test_create_custom_user(self):
        user = CustomUser.objects.create(email="testuser@example.com", nickname="testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.nickname, "testuser")


class AccountModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="user@example.com", nickname="testuser")

    def test_create_account(self):
        account = Account.objects.create(
            user=self.user,
            account_number="1234567890",
            bank_code="KB",
            account_type="SAVINGS",
            balance=1000.00
        )
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.account_number, "1234567890")
        self.assertEqual(account.get_bank_code_display(), "KB국민은행")
        self.assertEqual(account.account_type, "SAVINGS")
        self.assertEqual(account.balance, 1000.00)


class TransactionHistoryModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="user2@example.com", nickname="testuser2")
        self.account = Account.objects.create(
            user=self.user,
            account_number="9876543210",
            bank_code="NH",
            account_type="MINUS",
            balance=5000.00
        )
def test_create_transaction_history(self):
        transaction = TransactionHistory.objects.create(
            account=self.account,
            amount=1500.00,
            balance_after=3500.00,
            transaction_type="WITHDRAW",
            transaction_method="ATM",
            details="Test ATM withdrawal"
        )
        self.assertEqual(transaction.account, self.account)
        self.assertEqual(transaction.amount, 1500.00)
        self.assertEqual(transaction.balance_after, 3500.00)
        self.assertEqual(transaction.transaction_type, "WITHDRAW")
        self.assertEqual(transaction.transaction_method, "ATM")
        self.assertEqual(transaction.details, "Test ATM withdrawal")