from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import *


def index(request):
    user = request.user
    return render(request, 'account/index.html', {'user':user})

def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    # redirect back to index if authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect('index')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    # if 
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('index')
    else:
        return render(request, 'account/login.html', locals())

def register(request):
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CreatUserForm()

    return render(request,'account/register.html',{'form':form})
