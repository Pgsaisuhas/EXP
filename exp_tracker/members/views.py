from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['user_name']
        pass1 = request.POST['password1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            usena = user.username
            # return render(request, "home/index.html",{
            #     'username': usena,
            # })
            return redirect('/')

        else:
            messages.error(request, "Bad credentials")
            return redirect("/")

    return render(request, 'authenticate/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['user_name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        cpass = request.POST['password2']

        if pass1 == cpass:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.name = username

            myuser.save()
            messages.success(request, "Your account has ben successfully created.")

            return redirect('/members/login_user')
        else:
            messages.error(request, "The passwords do not match.")

    return render(request, 'authenticate/signup.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/home')