# Generated by Django 5.1.2 on 2024-11-04 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactionhistory",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accounts_transactions_history",
                to="accounts.account",
            ),
        ),
    ]