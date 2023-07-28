from django.urls import path, include
from . import views
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
]