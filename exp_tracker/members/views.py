from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# ? Import necessary modules and functions for rendering views, user authentication, and displaying messages.

# ? Define Views for User Authentication

def login_user(request):
    # * View function for user login.
    
    if request.method == "POST":
        # ! Handle POST request for user login.
        username = request.POST['user_name']
        pass1 = request.POST['password1']

        # ! Authenticate user credentials.
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            # ! If authentication is successful, log the user in and redirect to the home page.
            login(request, user)
            usena = user.username
            return redirect('/home/')
        else:
            # ! If authentication fails, display an error message and redirect back to the login page.
            messages.error(request, "Bad credentials")
            return redirect("/")

    # ! Render the 'login.html' template for displaying the login form.
    return render(request, 'authenticate/login.html')

def signup(request):
    # * View function for user signup.
    
    if request.method == "POST":
        # ! Handle POST request for user signup.
        username = request.POST['user_name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        cpass = request.POST['password2']

        if pass1 == cpass:
            # ! Create a new user using the provided credentials.
            myuser = User.objects.create_user(username, email, pass1)
            myuser.name = username

            myuser.save()
            messages.success(request, "Your account has been successfully created.")

            # ! Redirect to the login page.
            return redirect('/members/login_user')
        else:
            # ! If passwords do not match, display an error message.
            messages.error(request, "The passwords do not match.")

    # * Render the 'signup.html' template for displaying the signup form.
    return render(request, 'authenticate/signup.html')

def signout(request):
    # * View function for user signout.
    
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    
    # * Redirect to the home page.
    return render(request, 'authenticate/signout.html')
