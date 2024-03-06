from django.urls import path
from . import views

# ? URL Patterns for Routing

urlpatterns = [

    
    # ! Route for the default page, mapped to the 'index' view function.
    path("home/", views.index, name="index"),
    
    path("home/analytics", views.analytics, name="analytics"),
    # ! Route for the 'home' page, mapped to the 'home' view function.
    path('', views.home, name="home"),

    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
