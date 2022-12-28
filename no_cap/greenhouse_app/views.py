from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .models import Token_storage
from html.parser import HTMLParser
import requests


def login_home(request):
    # if request.method == 'GET':
    #     response = requests.get("http://127.0.0.1:8000/handle_csv/")
    #     print(response.text)
    #     return render(request, "greenhouse_app/login_home.html")
    # else:
    return render(request, "greenhouse_app/login_home.html")
        # return render(request, "greenhouse_app/login_home.html")

def show_seedling(request, getHex):
    print(getHex)
    return render(request, "greenhouse_app/show_seedling.html")

# class TokenStorage(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         for attr, val in attrs:
#             if attr == "hidden" and tag == "span":
#                 copyHash = val
#                 print(copyHash)
#         return copyHash



# def token_storage(request):
#     with open("/templates/token_generation.html", mode="r", encoding="utf-8") as html_file:
#         html_content = html_file.read()
#     token_value = TokenStorage()
#     token_value.feed(html_content)
#     # if request.method == 'POST':
#     # token_value = request.POST['writeToDom']

#     new_token = Token_storage(token_value=token_value)
#     new_token.create()
#     # new_token.save()
#     return render(request, "token_generation.html", {})



def signup(request):
    # if request.method == "GET":
    #     return render(request, "greenhouse_app/signup.html")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirmpw = request.POST['confirmpw']
# BELOW validations
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
    
