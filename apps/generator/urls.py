from django.urls import path
from . import views

urlpatterns = [
    path('generate_password/', views.generate_password, name='generate_password'),
    path('passwords/', views.password_list, name='passwords'),
    ]