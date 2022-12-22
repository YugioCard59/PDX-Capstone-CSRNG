from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

def login_home(request):
    return render(request, "greenhouse_app/login_home.html" )

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirmpw = request.POST['confirmpw']
        myuser = User.objects.create_user(username, email, password)
        myuser.username = username
        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        
    return render(request, "greenhouse_app/signin.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "login_home.html", {'username': username})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('login_home')
# MUST KEEP GREENHOUSE APP/ bc defined in urls
    return render(request, "greenhouse_app/signin.html")

def signout(request):
    pass
