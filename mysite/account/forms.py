from dataclasses import field
from django.forms import ModelForm
from django.forms import DateTimeField
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreatUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User 
        fields = ['username','email','password1','password2','first_name','last_name']

class CreatDriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['vehicle_type','license_plate_number','max_number_passengers','special_request']

class RideRequestForm(ModelForm):
    arrival_time = DateTimeField(input_formats=["%m-%d-%Y %H:%M"],help_text="Please using format: <em>MM-DD-YYYY HH:mm<em>")
    class Meta:
        model = Ride
        fields = ['shared_or_not','destination','arrival_time','vehicle_type','total_passengers','special_request']
