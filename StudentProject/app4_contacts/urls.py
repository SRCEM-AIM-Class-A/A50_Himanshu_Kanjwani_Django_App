from django.contrib import admin
from django.urls import path
from app4_contacts import views

urlpatterns = [
    path('',views.contacts, name='contacts'),
]