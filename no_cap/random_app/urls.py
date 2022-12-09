from django.urls import path
from . import views



urlpatterns = [
    # path('', views.welcome, name = 'welcome'),
    path('', views.upload_file, name='upload_file'), 
    # upload_file located in welcome.html
    
]