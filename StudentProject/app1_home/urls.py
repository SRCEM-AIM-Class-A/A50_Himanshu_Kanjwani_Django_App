from django.contrib import admin
from django.urls import path
from app1_home import views

urlpatterns = [
    path('',views.home, name='home'),
]