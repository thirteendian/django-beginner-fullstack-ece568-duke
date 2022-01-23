from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreatUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
