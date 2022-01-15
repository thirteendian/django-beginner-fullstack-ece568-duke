from urllib import request
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('login/',views.djlogin,name='login'),
=======
    path('',views.index,name='index'), #<a href="{% url 'index' %}">Home</a>. Link to this page in HTML
>>>>>>> 27d2912d9b8407105e1bef2011080bc563f0a686
]
