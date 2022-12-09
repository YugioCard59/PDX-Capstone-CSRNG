from django.urls import path
from . import views



urlpatterns = [
    # path('', views.welcome, name = 'welcome'),
    path('', views.upload_csvfile, name='upload_csvfile'),
    
]