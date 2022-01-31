from dataclasses import field
from django.forms import ModelForm,Form
from django.forms import DateTimeField, IntegerField,CharField
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


class SharerRequestForm(Form):
    destination = CharField(max_length = 60,help_text="Destination")
    earliest = DateTimeField(input_formats=["%m-%d-%Y %H:%M"],help_text="Earliest Time You Required, Please using format: <em>MM-DD-YYYY HH:mm<em>")
    latest = DateTimeField(input_formats=["%m-%d-%Y %H:%M"],help_text="Latest Time Your Required Please using format: <em>MM-DD-YYYY HH:mm<em>")
    number_of_passengers = IntegerField(help_text="Number Of Passengers")
    
