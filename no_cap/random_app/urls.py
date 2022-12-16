from django.urls import path
from . import views



urlpatterns = [
    path('', views.upload_file, name='upload_file'), 
    # above: upload_file located in welcome.html
    path('token_generation/', views.token_generation, name='token_generation'),
    path('token_generation/handle_csv/', views.handle_csv, name="handle_csv")
]