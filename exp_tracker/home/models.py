from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TYPE = (
    ('income', 'income'),
    ('expense', 'expense'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField(default=0, max_length=10)
    expenses = models.FloatField(default=0)
    balance = models.FloatField(default=0)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100, choices=TYPE)
    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User: {self.user.username}, {self.transaction_type} - {self.amount} on {self.date}"

