from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('<int:id>/index/',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout,name = 'logout'),
    path('<int:id>/register_driver/',views.register_driver,name = 'registerdriver'),
    path('<int:id>/request/',views.request,name='request'),
    path('<int:id>/view_owned_ride/',views.view_owned_ride,name='view_owned_ride'),
    path('<int:id>/view_shared_ride/',views.view_shared_ride,name='view_shared_ride'),
    path('<int:id>/view_drive_ride/',views.view_drive_ride,name='view_drive_ride'),
    path('<int:id>/edituserinfo/',views.edit_user_info,name='edituserinfo'),
    path('<int:id>/editdriverinfo/',views.edit_driver_info,name='editdriverinfo')
]
