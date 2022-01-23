from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('<int:id>/index/',views.index,name = 'index'),
    path('register', views.register, name='register'),
]
