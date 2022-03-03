from django.contrib import admin
from django.urls import path
from icai import views

urlpatterns = [
    path('', views.home, name='icai'),
    path('login', views.login, name='login'),
    path('sessionover', views.over, name='over'),
    path('golive', views.sessionlive, name='live_session'),
    path('ques', views.qus_send, name='auestionsent')
]
