from django.shortcuts import render, redirect
from . import models

# * Import required modules and functions for rendering views and interacting with models.

# ? Define Views for Handling User Requests

def index(request):
    # * View function for the default 'index' page.
    
    # ! Fetch the user's profile from the database.
    profile = models.Profile.objects.filter(user=request.user).first()
    
    # ! Fetch the user's expenses and order them by descending ID (latest first).
    expenses = models.Expense.objects.filter(user=request.user).order_by('-id')
    
    # ! Check if the request method is POST (form submission).
    if request.method == 'POST':
        #  * Extract data from the POST request.
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        
        #  * Create a new Expense object with the extracted data.
        expense = models.Expense(name=text, amount=amount, expense_type=expense_type, user=request.user)
        
        # * Save the new expense to the database.
        expense.save()

        # * Update user profile data based on the expense type.
        if expense_type == "income":
            profile.balance += float(amount)
            profile.income += float(amount)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
        
        # ? Save the updated profile data.
        profile.save()
        
        # ? Redirect the user back to the index page.
        return redirect('/')

    # ? Render the 'index.html' template with the fetched data.
    return render(request, 'home/index.html', {
        'profile': profile,
        'expenses': expenses,
    })

def home(request):
    # * View function for the 'home' page.
    
    # * Render the 'home.html' template.
    return render(request, 'home/home.html')
