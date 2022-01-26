from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth,messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *



def index(request):
    my_user = myUser.objects.get(user = request.user)
    #my_user = myUser.objects.get(id = user.id)
    #return render(request, 'account/index.html', {'user':user})
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
            my_user = myUser.objects.create(user = user)
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
            return redirect('index')
    else:
        form = CreatDriverForm()

    return render(request,'account/register_driver.html',{'form':form})

def request(request):

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
            return redirect('index') # 'view/myride'
    else:
            form = RideRequestForm()
    return render(request,'account/require.html',{'form':form})

def view_owned_ride(request): 
    all_ride = Ride.objects.all()
    return render(request,'account/view_owned_ride.html',{'all_ride':all_ride})

def view_shared_ride(request):
    return

def view_drive_ride(request):
    return
