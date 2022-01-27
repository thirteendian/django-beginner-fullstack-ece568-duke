from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth,messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .models import *
from .forms import *



def index(request,id):
    my_user = myUser.objects.get(user = request.user)
    if my_user.is_driver == False:
        return render(request, 'account/index.html', {'myuser':my_user})
    else:
        driver = Driver.objects.get(user=request.user)
        return render(request, 'account/index_driver.html', {'driver':driver})

def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    # redirect back to index if authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect('%s/index'% request.user.id)# This is also correct
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    # if 
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('index', id=request.user.id)
    else:
        messages.info(request,'Wrong username or password')
        return render(request, 'account/login.html', locals())

def register(request):
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            my_user = myUser.objects.create(user = user)
            my_user.save()
            return redirect('login')
    else:
        form = CreatUserForm()

    return render(request,'account/register.html',{'form':form})

def edit_user_info(request,id):
    user=request.user
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        form_password = PasswordChangeForm(user,request.POST)
        if form.is_valid() and form_password.is_valid():
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user=form_password.save()
            update_session_auth_hash(request,user)
            return redirect('index',id= request.user.id)
    else:
        form = EditUserForm()
        form_password = PasswordChangeForm(user)
        return render(request,'account/edituserinfo.html',{'form':form,'form_password':form_password,'user':user})


def edit_driver_info(request,id):
    my_driver=Driver.objects.get(user=request.user)
    if request.method == 'POST':
        form = CreatDriverForm(request.POST)
        if form.is_valid():             
            my_driver.vehicle_type = form.cleaned_data['vehicle_type']
            my_driver.license_plate_number = form.cleaned_data['license_plate_number']
            my_driver.max_number_passengers = form.cleaned_data['max_number_passengers']
            my_driver.special_request = form.cleaned_data['special_request']
            my_driver.save()
            return redirect('index' ,id= request.user.id )
    else:
        form = CreatDriverForm()
    return render(request,'account/editdriverinfo.html',{'form':form,'my_driver':my_driver})

            

def register_driver(request,id):
    user = request.user
    my_user = get_object_or_404(myUser,user = user)
    if request.method == 'POST':
        form = CreatDriverForm(request.POST)

        if form.is_valid():
            
            
            my_driver = Driver.objects.create(user=user)
            
            my_driver.vehicle_type = form.cleaned_data['vehicle_type']
            my_driver.license_plate_number = form.cleaned_data['license_plate_number']
            my_driver.max_number_passengers = form.cleaned_data['max_number_passengers']
            my_driver.special_request = form.cleaned_data['special_request']
       
            my_driver.save()
            myUser.objects.filter(user=user).update(is_driver=True)
            #my_user.is_driver = True

            #my_driver.myuser = my_user
            #my_driver.save()
            return redirect('index', id = user.id)
    else:
        form = CreatDriverForm()

    return render(request,'account/register_driver.html',{'form':form,'user':user})

def request(request,id):

    if request.method == 'POST':
        user= request.user
        form = RideRequestForm(request.POST)
        if form.is_valid():
            my_ride = Ride.objects.create(owner=user)
            my_ride.destination = form.cleaned_data['destination']
            my_ride.arrival_time = form.cleaned_data['arrival_time']
            my_ride.vehicle_type = form.cleaned_data['vehicle_type']
            my_ride.total_passengers = form.cleaned_data['total_passengers']
            my_ride.special_request = form.cleaned_data['special_request']
            my_ride.shared_or_not = form.cleaned_data['shared_or_not']
            my_ride.save()
            return redirect('index', id=user.id)
    else:
            form = RideRequestForm()
    return render(request,'account/request.html',{'form':form,'user':request.user})


def view_owned_ride(request,id): 
    all_ride = Ride.objects.all().filter(owner = request.user)
    return render(request,'account/view_owned_ride.html',{'all_ride':all_ride,'user':request.user})

def view_shared_ride(request,id):
    return

def view_drive_ride(request,id):
    return
