from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import Token_storage
import os
from django.contrib.auth.decorators import login_required

def login_home(request):
    if request.method == "POST" and request.user.is_authenticated:
        getHash = request.POST['writeToDom']
        print(f"from login view writetodom: {getHash}")
        new_token_form = Token_storage(token_value=getHash, token_user=request.user)
        new_token_form.save()

        dir = './media/random_app/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        path = "./static/cleanedList.json"
        isFile = os.path.isfile(path)
        print(f"from login view does json exists: {isFile}")
        if isFile:
            os.remove(path)

        return redirect("greenhouse_app:show_seedling")

    elif request.method == "POST":
        getHash = request.POST['writeToDom']
        print(f"from login view writetodom: {getHash}")
        request.session['getHash'] = getHash
        dir = './media/random_app/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        path = "./static/cleanedList.json"
        isFile = os.path.isfile(path)
        if isFile:
            os.remove(path)
        return render(request, "greenhouse_app/signin.html", {"getHash": getHash})
    
    return render(request, "greenhouse_app/login_home.html")

@login_required
def show_seedling(request):
    dir = './media/random_app/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    path = "./static/cleanedList.json"
    isFile = os.path.isfile(path)
    print(f"from show seedling view does json exist: {isFile}")
    if isFile:
        os.remove(path)
    if request.method == "GET" and request.user.is_authenticated:
        try:
            seedling_list = Token_storage.objects.filter(token_user=request.user)
            content = {
                'seedling_list': seedling_list
            }
            getHash = request.session['getHash']
            for element in seedling_list:
                if element.token_value == getHash:
                    element.delete()
                    new_token_form = Token_storage(token_value=getHash, token_user=request.user)
                    new_token_form.save()
   
        except:
            seedling_list = Token_storage.objects.filter(token_user=request.user)
            content = {
                'seedling_list': seedling_list
            }
            return render(request, "greenhouse_app/show_seedling.html", content)
     
        return render(request, "greenhouse_app/show_seedling.html", content)


def delete_seedling(request):
    seedling_list = Token_storage.objects.filter(token_user=request.user)
    content = {
        'seedling_list': seedling_list
        }
    if request.method == 'POST':
        delete_list = request.POST.getlist("seedDelete")
        print(delete_list)
        for seedling_id in delete_list:
            Token_storage.objects.get(pk=int(seedling_id))
            Token_storage.objects.get(pk=int(seedling_id)).delete()
  
    return render(request, "greenhouse_app/show_seedling.html", content)

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

    if request.user.is_authenticated:
        
        logout(request)
        messages.info(
            request, "You are now logged out."
        )
        return redirect('greenhouse_app:login_home')
    
    elif request.method == "POST":
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

    return render(request, "greenhouse_app/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('random_app:upload_file')

    
