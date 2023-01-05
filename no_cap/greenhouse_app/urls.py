from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "greenhouse_app"

urlpatterns = [
    path('', views.login_home, name="login_home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    # path('token_storage/', views.token_storage, name="token_storage"),
    # path('storage/', views.TokenStorage, name="storage"),
    # path('show_seedling/<str:getHashHex>/', views.show_seedling, name="show_seedling"),
    path('show_seedling/', views.show_seedling, name="show_seedling"),
]