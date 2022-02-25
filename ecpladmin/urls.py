from django.contrib import admin
from django.urls import path
from ecpladmin import views

urlpatterns = [
    path('ecpladmin', views.admin, name='ecpladmin'),
    path('dashboard', views.dashboard, name='dashboard')
]
