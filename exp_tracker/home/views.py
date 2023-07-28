from django.shortcuts import render,redirect
from . import models
# Create your views here.
def index(request):
    profile = models.Profile.objects.filter(user = request.user).first()
    expenses = models.Expense.objects.filter(user = request.user).order_by('-id')
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        expense = models.Expense(name=text, amount=amount, expense_type=expense_type, user = request.user)
        expense.save()

        if expense_type == "income":
            profile.balance += float(amount)
            profile.income += float(amount)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
        
        profile.save()
        return redirect('/')


    context = {
        'profile': profile,
        'expenses':expenses,
    }
    return render(request, 'home/index.html', context)

def home(request):
    return render(request, 'home/home.html')