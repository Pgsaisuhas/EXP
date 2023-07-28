from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPE = (
    ('income', 'income'),
    ('expense', 'expense'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField(default=0,max_length=10)
    expenses = models.FloatField(default=0)
    balance = models.FloatField(default=0)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount  = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE)


    def __str__(self):
        return self.name