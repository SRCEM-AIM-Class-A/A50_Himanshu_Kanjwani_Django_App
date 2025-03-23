from django.contrib import admin
from django.urls import path
from app2_about import views

urlpatterns = [
    path('',views.about, name='about'),
]