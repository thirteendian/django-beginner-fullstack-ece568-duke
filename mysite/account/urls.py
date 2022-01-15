from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.djlogin,name='login'),
]
