from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreatUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User 
        fields = ['username','email','password1','password2','first_name','last_name']

class CreatDriverForm(ModelForm):
    class Meta:
        model = Driver
        is_driver = True
        fields = ['vehicle_type','license_plate_number','max_number_passengers','special_request']