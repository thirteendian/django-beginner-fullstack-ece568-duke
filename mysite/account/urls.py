from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('accounts/login/',views.login),# 'accounts/login' is the default page of Django login page
]
