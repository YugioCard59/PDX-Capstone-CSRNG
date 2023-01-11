from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "greenhouse_app"

urlpatterns = [
    path('', views.login_home, name="login_home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('show_seedling/', views.show_seedling, name="show_seedling"),
    path('delete_seedling/', views.delete_seedling, name="delete_seedling"),
]