from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import Token_storage
from .forms import StorageForm
from html.parser import HTMLParser
import requests
import json


def login_home(request):
    if request.method == "POST" and User.is_authenticated:
        getHash = request.POST['writeToDom']
        print(getHash)
        # print(content)
        # print(type(content))
        # json_get_Hash = getHash.json()
        # json_getHash = json.loads(json_get_Hash)
        # print(type(json_getHash))
        # new_toke = Token_storage(token_value=getHash)= getHash
        new_token_form = Token_storage(token_value=getHash, )
        # if new_token_form.is_valid():
        new_token_form.save()
    return render(request, "greenhouse_app/login_home.html", {'new_token_form': new_token_form})
        # return render(request, "greenhouse_app/login_home.html")

def show_seedling(request):
    # if request.method == "POST":
    #     print(getHash)
    #     token_value = getHash
    #     new_token = Token_storage(token_value=token_value)
    #     new_token.create()
    #     new_token.save()
    

    #     print(request.body)
    #     getHash = json.loads(request.body.decode("utf-8"))
    #     print(getHash)
    # getHash = request.POST.get("jsonField", "")
    # getHashex = request.POST.get('getHashHex')
    # print(request.GET.get('getHashHex'))
    # print(request.body)
        
    # # getHashHex = request.POST['getHashHex']
    #     # geHashHex = {'getHashHex': getHashHex}
    # print(getHashex)
    # print(json.loads(getHashHex))
    # print(getHashHex)
    # return JsonResponse(request.body)
    return render(request, "greenhouse_app/show_seedling.html")





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
    
