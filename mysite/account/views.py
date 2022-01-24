from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import myUser,Driver
from .forms import *


def index(request):
    user = myUser.objects.filter(id = request.user.id)
    if user.is_driver == False:
        return render(request, 'account/index.html', {'user':user})
    else:
        return render(request, 'account/index_driver.html', {'user':user})

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

def register_driver(request):
    if request.method == 'POST':
        form = CreatDriverForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = CreatDriverForm()

    return render(request,'account/register_driver.html',{'form':form})