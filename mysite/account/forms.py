from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreatUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = myUser
        fields = ['username','email','password1','password2','first_name','last_name']

class CreatDriverForm(CreatUserForm):
    class Meta(CreatUserForm):
        model = Driver
        is_driver = 1
        fields = ['vehicle_type','license_plate_number','max_number_passengers','special_request']