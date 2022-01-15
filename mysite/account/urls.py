from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'), #<a href="{% url 'index' %}">Home</a>. Link to this page in HTML
]
