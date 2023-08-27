from django.contrib import admin
from . import models
from .models import Profile, Expense, Transaction


# * Registered 2 main models for admin panel access.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'income', 'expenses', 'balance')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount', 'expense_type')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Transaction)