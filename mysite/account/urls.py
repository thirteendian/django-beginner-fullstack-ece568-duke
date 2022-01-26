from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('index/',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout,name = 'logout'),
    path('register_driver/',views.register_driver,name = 'registerdriver'),
    path('request/',views.request,name='request'),
    path('view_owned_ride/',views.view_owned_ride,name='view_owned_ride'),
    path('view_shared_ride/',views.view_shared_ride,name='view_shared_ride'),
    path('view_drive_ride/',views.view_drive_ride,name='view_drive_ride'),
]
