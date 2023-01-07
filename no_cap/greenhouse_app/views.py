from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import Token_storage
import os, glob

def login_home(request):
    if request.method == "POST" and request.user.is_authenticated:
        getHash = request.POST['writeToDom']
        print(getHash)
        new_token_form = Token_storage(token_value=getHash, token_user=request.user)
        new_token_form.save()
        return render(request, "greenhouse_app/login_home.html", {'new_token_form': new_token_form})
    return render(request, "greenhouse_app/login_home.html")

def show_seedling(request):
    dir = './media/random_app/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    path = "./static/cleanedList.json"
    isFile = os.path.isfile(path)
    print(isFile)
    if isFile:
        os.remove(path)

    seedling_list = Token_storage.objects.all()
    
    return render(request, "greenhouse_app/show_seedling.html", {'seedling_list': seedling_list})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirmpw = request.POST['confirmpw']
# BELOW KEEP! validations
        # if User.objects.filter(username=username) or User.objects.filter(email=email):
        #     messages.error(request, "Sign Up Failed! Please enter a different username and/or email")
        #     return redirect('greenhouse_app:login')
        # if len(username)>10:
        #     messages.error(request, "Username must be under 10 alphanumeric characters")
        # if password != confirmpw:
        #     messages.error(request, "Password did not match!")
        # if not username.isalnum():
        #     messages.error(request, "Username must be alphanumeric characters")
        #     return redirect('greenhouse_app:login_home')
        myuser = User.objects.create_user(username, email, password)
        myuser.username = username
        myuser.save()
        messages.success(
            request, "Your account has been successfully created!")
        return redirect('greenhouse_app:signin')
    
    return render(request, "greenhouse_app/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "greenhouse_app/login_home.html", {'username': username})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('greenhouse_app:login_home')
# MUST KEEP GREENHOUSE APP/ bc defined in urls
    return render(request, "greenhouse_app/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('greenhouse_app:login_home')
    
