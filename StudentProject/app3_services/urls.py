from django.contrib import admin
from django.urls import path
from app3_services import views

urlpatterns = [
    path('',views.services, name='services'),
]