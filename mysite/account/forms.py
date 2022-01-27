from dataclasses import field
from django.forms import ModelForm
from django.forms import DateTimeField
from django.forms import ChoiceField
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .models import *

class CreatUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User 
        fields = ['username','email','first_name','last_name','password1','password2']

class EditUserForm(UserCreationForm):
    password1 = None
    password2 = None
    class Meta(UserCreationForm):
        model=User
        fields = ['email','first_name','last_name']

        
class CreatDriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['vehicle_type','license_plate_number','max_number_passengers','special_request']

class RideRequestForm(ModelForm):
    arrival_time = DateTimeField(input_formats=["%m-%d-%Y %H:%M"],help_text="Please using format: <em>MM-DD-YYYY HH:mm<em>")
    class Meta:
        model = Ride
        fields = ['shared_or_not','destination','arrival_time','vehicle_type','total_passengers','special_request']

        
        
'''
class EditChoiceForm(ModelForm):
    OPTIONS=[
        ('Password','user_password'),
        ('Email Address','user_email'),
        ('First Name','user_firstname'),
        ('Last Name','user_lastname'),
        ('Vehicle Type','user_vehicle_type'),
        ('License Plate Number','user_license_plate_number'),
        ('Max Passengers','user_max_passengers'),
        ('Special Request','user_special_request')
    ]
    choice = forms.ChoiceField(required=True,choices=OPTIONS)
class EditInputForm(ModelForm):
     input_value = forms.CharField(max_length=20,choices = )
'''
