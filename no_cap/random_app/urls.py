from django.urls import path
from . import views

app_name =  "random_app"

urlpatterns = [
    path('', views.upload_file, name='upload_file'), 
    path('token_generation/', views.token_generation, name='token_generation'),
    path('handle_csv/', views.handle_csv, name="handle_csv"),
 
]