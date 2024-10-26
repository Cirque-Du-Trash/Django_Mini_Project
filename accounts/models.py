from django.db import models
from django.conf import settings

class Account(models.Model):
    BANK_CHOICES = [
        ('KB', 'KB국민은행'),
        ('NH', 'NH농협은행'),
        ('IBK', 'IBK기업은행'),
        ('KA', '카카오뱅크'),
        # 필요에 따라 더 추가
    ]
    ACCOUNT_TYPES = [
        ('SAVINGS', '입출금통장'),
        ('MINUS', '마이너스통장'),
        # 필요에 따라 더 추가
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    bank_code = models.CharField(max_length=3, choices=BANK_CHOICES)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.name}'s {self.get_bank_code_display()} Account"