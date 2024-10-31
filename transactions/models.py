from django.db import models
from accounts.models import Account

class TransactionHistory(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', '입금'),
        ('WITHDRAW', '출금'),
    ]
    TRANSACTION_METHODS = [
        ('CASH', '현금'),
        ('TRANSFER', '계좌이체'),
        ('AUTO', '자동이체'),
        ('CARD', '카드결제'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction_transactions_histories')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_detail = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    method = models.CharField(max_length=10, choices=TRANSACTION_METHODS)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.user.name}'s {self.get_transaction_type_display()} of {self.amount}"