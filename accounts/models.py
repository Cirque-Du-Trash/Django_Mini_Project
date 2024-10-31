from django.db import models
from django.conf import settings

class CustomUser(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)

    def str(self):
        return self.nickname


class Account(models.Model):
    BANK_CHOICES = [
        ('KB', 'KB국민은행'),
        ('NH', 'NH농협은행'),
        ('IBK', 'IBK기업은행'),
        ('KA', '카카오뱅크'),
    ]
    ACCOUNT_TYPES = [
        ('SAVINGS', '입출금통장'),
        ('MINUS', '마이너스통장'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    bank_code = models.CharField(max_length=3, choices=BANK_CHOICES)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def str(self):
        return f"{self.user.nickname}'s {self.get_bank_code_display()} Account"


class TransactionHistory(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', '입금'),
        ('WITHDRAW', '출금'),
    ]
    TRANSACTION_METHODS = [
        ('ONLINE', '온라인 송금'),
        ('ATM', 'ATM 거래'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='acconts_transactions_hitories')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance_after = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=255, choices=TRANSACTION_TYPES)
    transaction_method = models.CharField(max_length=255, choices=TRANSACTION_METHODS)
    details = models.TextField()

    def str(self):
        return f"{self.transaction_type} of {self.amount} on {self.account}"