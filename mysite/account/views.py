from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth,messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import myUser,Driver
from .forms import *



def index(request):
    my_user = myUser.objects.get(user = request.user)
    #my_user = myUser.objects.get(id = user.id)
    #return render(request, 'account/index.html', {'user':user})
    if my_user.is_driver == False:
        return render(request, 'account/index.html', {'user':my_user})
    else:
        driver = Driver.objects.get(user=request.user)
        return render(request, 'account/index_driver.html', {'user':driver})

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
        messages.info(request,'Wrong username or password')
        return render(request, 'account/login.html', locals())

def register(request):
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            my_user = myUser(user = user)
            my_user.save()
            return redirect('login')
    else:
        form = CreatUserForm()

    return render(request,'account/register.html',{'form':form})

def register_driver(request):
    user = request.user
    my_user = get_object_or_404(myUser,user = user)
    if request.method == 'POST':
        form = CreatDriverForm(request.POST)

        if form.is_valid():
            
            
            my_driver = Driver(user=user)
            
            my_driver.vehicle_type = form.cleaned_data['vecicle_type']
            my_driver.license_plate_number = form.cleaned_data['license_plate_number']
            my_driver.max_number_passengers = form.cleaned_data['max_number_passengers']
            my_driver.special_request = form.cleaned_data['special_request']
       
            my_driver.save()
            my_user.is_driver = True

            #my_driver.myuser = my_user
            #my_driver.save()
            return redirect('index')
    else:
        form = CreatDriverForm()

    return render(request,'account/register_driver.html',{'form':form})