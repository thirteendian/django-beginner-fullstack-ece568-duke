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
    path('<int:id>/editdriverinfo/',views.edit_driver_info,name='editdriverinfo'),
    path('cancel/<int:id>/',views.cancel_ride,name='cancelride'),
    path('edit/<int:id>/',views.edit_ride,name='editride'),
    path('<int:id>/driver_search/',views.driver_search,name='driversearch'),
    path('confirm_ride/<int:id>/',views.confirm_ride,name = 'confirmride'),
    path('complete_ride/<int:id>/',views.complete_ride,name='completeride'),
    path('<int:id>/join_ride/',views.join_ride,name='joinride'),
    path('jointhis_ride/<int:id>/',views.join_this_ride,name='jointhisride'),
    #path('<int:id>/edit_sharer_filter',views.edit_sharer_filter,name='editsharerfilter'),
    path('quit_this_ride/<int:id>',views.quit_this_ride,name='quitthisride')
]
