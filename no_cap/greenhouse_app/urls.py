from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_home, name="login_home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),

]