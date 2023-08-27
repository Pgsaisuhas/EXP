from django.urls import path, include
from . import views

# ? Define URL Patterns for User Authentication

urlpatterns = [
    # ! Route for user login, mapped to the 'login_user' view function.
    path('login_user/', views.login_user, name='login'),
    
    # ! Route for user signup, mapped to the 'signup' view function.
    path('signup/', views.signup, name='signup'),
    
    # ! Route for user signout, mapped to the 'signout' view function.
    path('signout/', views.signout, name='signout'),
]
