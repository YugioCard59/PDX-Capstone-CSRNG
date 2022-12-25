from django.urls import path
from . import views

app_name =  "random_app"

urlpatterns = [
    path('', views.upload_file, name='upload_file'), 
    # above: upload_file located in welcome.html
    path('token_generation/', views.token_generation, name='token_generation'),
    path('handle_csv/', views.handle_csv, name="handle_csv"),
    # path('delete_tmp/', views.delete_temp, name="delete_tmp"),
    # path('test/', views.test, name="test"),
]