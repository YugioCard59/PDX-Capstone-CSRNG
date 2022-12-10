from django.urls import path
from . import views



urlpatterns = [
    path('', views.upload_file, name='upload_file'), 
    # above: upload_file located in welcome.html
    
]