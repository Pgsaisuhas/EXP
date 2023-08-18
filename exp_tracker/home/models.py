from django.db import models
from django.contrib.auth.models import User

# ? Define choices for categorizing expenses as 'income' or 'expense'.
TYPE = (
    ('income', 'income'),
    ('expense', 'expense'),
)

#  * User Profile Model
class Profile(models.Model):
    # ? Represents user-specific financial data.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ! Connects user profile to a user account.
    income = models.FloatField(default=0, max_length=10)  # ! Total income earned by the user.
    expenses = models.FloatField(default=0)  # ! Total expenses incurred by the user.
    balance = models.FloatField(default=0)  # ! Current balance of the user's financial account.

# Expense Model
class Expense(models.Model):
    #  * Represents a financial expense.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ! Connects expense to a user account.
    name = models.CharField(max_length=100)  # ! Name or description of the expense.
    amount = models.FloatField()  # ! The monetary amount of the expense.
    expense_type = models.CharField(max_length=100, choices=TYPE)  # ! Categorizes the expense as 'income' or 'expense'.

    def __str__(self):
        # ? Returns a string representation of the expense object (its name).
        return self.name
