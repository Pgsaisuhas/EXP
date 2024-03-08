from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Expense, Profile, Transaction
from django.db import connection
from django.http import Http404
import csv
from django.http import JsonResponse
import json
import datetime
# * Import required modules and functions for rendering views and interacting with models.

# ? Define Views for Handling User Requests

def landing(request):
    return render(request, 'home/landingpage.html')


def index(request):
    # * View function for the default 'index' page.
    
    # ! Fetch the user's profile from the database.
    profile = models.Profile.objects.filter(user=request.user).first()
    
    # ! Fetch the user's expenses and order them by descending ID (latest first).
    expenses = models.Expense.objects.filter(user=request.user).order_by('-id')
    
    # ! Check if the request method is POST (form submission).
    if request.method == 'POST':
        #  * Extract data from the POST request.
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        if request.POST.get('type'):
            expense_type = "expense"
        else:
            expense_type = "income"
        date = request.POST.get('date')

        #  * Create a new Expense object with the extracted data.
        expense = models.Expense(name=name, amount=amount, expense_type=expense_type, user=request.user, date=date)
        
        # * Save the new expense to the database.
        expense.save()

        # * Update user profile data based on the expense type.
        if expense_type == "income":
            profile.balance += float(amount)
            profile.income += float(amount)
            with open('income.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                field = [profile.user, amount, date]
                writer.writerow(field)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
            with open('expense.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                field = [profile.user, amount, date]
                writer.writerow(field)
        
        # ? Save the updated profile data.
        profile.save()



        transaction = Transaction(
            user=request.user,
            transaction_type=expense_type,
            amount=amount,
            date=date
        )
        transaction.save()
        
        # ? Redirect the user back to the index page.
        return redirect('/home/')

    # ? Render the 'index.html' template with the fetched data.
    return render(request, 'home/index.html', {
        'profile': profile,
        'expenses': expenses,
    })

def home(request):
    # * View function for the 'home' page.
    
    # * Render the 'home.html' template.
    return render(request, 'home/home.html')





def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    profile = Profile.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        expense_amount = expense.amount
        
        if expense.expense_type == 'income':
            profile.income -= expense_amount
            profile.balance -= expense_amount
        else:
            profile.expenses -= expense_amount
            profile.balance += expense_amount  # Add back the amount to balance
        
        profile.save()
        
        # Delete the corresponding transaction if it exists
        transaction = Transaction.objects.filter(user=request.user, amount=expense_amount).first()
        if transaction:
            transaction.delete()
        
        expense.delete()
    
    return redirect('/home/')



from django.contrib.auth.decorators import login_required

@login_required
def analytics(request):
    user = request.user
    expenses_data = expenses_over_time(user)
    income_data = income_over_time(user)
    print(expenses_data, income_data)
    profile = Profile.objects.filter(user=request.user).first()

    final_dates = sorted(set(expenses_data[0] + income_data[0]))
    print(final_dates)
    combined_data = {
        'expense_dates'     : expenses_data[0],
        'Expenses'          : expenses_data[1],
        'income_dates'     : income_data[0],
        'final_dates'       : final_dates,
        'Incomes'           : income_data[1],
        'profile_balance'   : profile.balance,
        'profile_expense'   : profile.expenses,
        'profile_income'    : profile.income,
    }

    return render(request, 'home/chart.html', combined_data)

def expenses_over_time(user):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DATE(date) AS transaction_date, SUM(amount) AS total_income
            FROM home_transaction
            WHERE transaction_type = 'expense' AND user_id = %s
            GROUP BY DATE(date)
            ORDER BY DATE(date)
        """, [user.id])
        rows = cursor.fetchall()

    labels = []
    data = []
    
    for row in rows:
        labels.append(row[0].strftime("%d-%m-%Y"))
        data.append(row[1])
    return [labels, data]

def income_over_time(user):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DATE(date) AS transaction_date, SUM(amount) AS total_income
            FROM home_transaction
            WHERE transaction_type = 'income' AND user_id = %s
            GROUP BY DATE(date)
            ORDER BY DATE(date)
        """, [user.id])
        rows = cursor.fetchall()

    labels = []
    data = []

    for row in rows:
        labels.append(row[0].strftime("%d-%m-%Y"))
        data.append(row[1])

    return [labels, data]

