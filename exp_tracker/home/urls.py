from django.urls import path
from . import views

# ? URL Patterns for Routing

urlpatterns = [
    # ! Route for the default page, mapped to the 'index' view function.
    path("", views.index, name="index"),
    
    # ! Route for the 'home' page, mapped to the 'home' view function.
    path('home/', views.home, name="home")
]
