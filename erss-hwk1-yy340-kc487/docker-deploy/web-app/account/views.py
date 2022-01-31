from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth,messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.conf import settings
from django.core.mail import send_mail

from .models import *
from .forms import *


######################################################################################
# USER
######################################################################################
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
    else:
        if request.method == 'POST':
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
            my_ride.total_people=my_ride.total_passengers
            my_ride.save()
            return redirect('index', id=user.id)
    else:
            form = RideRequestForm()
    return render(request,'account/request.html',{'form':form,'user':request.user})


def view_owned_ride(request,id):
    my_user = myUser.objects.get(user = request.user)
    all_ride = Ride.objects.all().filter(owner = request.user)
    confirmed_ride = Ride.objects.all().filter(owner = request.user, status = 'Confirmed')
    open_ride = Ride.objects.all().filter(owner = request.user, status = 'Open')
    status = "All"
    if request.method == 'POST':
        view_filter = request.POST['all_open_or_confirmed']
        if view_filter == "All":
            status = "All"
            return redirect('view_owned_ride',id=id)
        elif view_filter == "Confirmed":
            status = "Confirmed"
            return render(request,'account/view_owned_ride.html',{'all_ride':confirmed_ride,'user':request.user,'status':status,'my_user':my_user})
        elif view_filter == "Open":
            status = "Open"
            return render(request,'account/view_owned_ride.html',{'all_ride':open_ride,'user':request.user,'status':status,'my_user':my_user})
    return render(request,'account/view_owned_ride.html',{'all_ride':all_ride,'user':request.user,'status':status,'my_user':my_user})


def edit_ride(request,id):
    user= request.user
    my_ride = Ride.objects.get(id=id)
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            my_ride.destination = form.cleaned_data['destination']
            my_ride.arrival_time = form.cleaned_data['arrival_time']
            my_ride.vehicle_type = form.cleaned_data['vehicle_type']
            my_ride.total_people=my_ride.total_people-my_ride.total_passengers
            my_ride.total_passengers = form.cleaned_data['total_passengers']
            my_ride.total_people=my_ride.total_people + my_ride.total_passengers
            my_ride.special_request = form.cleaned_data['special_request']
            my_ride.shared_or_not = form.cleaned_data['shared_or_not']
            
            if my_ride.shared_or_not == False:
                for sharer in my_ride.sharer.all():
                    my_ride.total_people-=sharer.total_sharers
                    sharer.total_sharers = None
                    sharer.save()
                my_ride.sharer.clear()
                
            my_ride.save()
            return redirect('view_owned_ride', id=user.id)
    else:
        form = RideRequestForm()
    return render(request,'account/edit_ride.html',{'form':form,'user':request.user,'old_ride':my_ride})


def cancel_ride(request,id):
    cancelled_ride = Ride.objects.get(id=id)
    user_id = cancelled_ride.owner.id
    for sharer in cancelled_ride.sharer.all():
        sharer.total_sharers = None
        sharer.save()
    cancelled_ride.delete()
    return redirect('view_owned_ride',id=user_id)

######################################################################################
# DRIVER
######################################################################################
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


def driver_search(request,id):
    user = User.objects.get(id=id)
    driver= Driver.objects.get(user=user)
    all_ride = Ride.objects.all().filter(status='Open',vehicle_type=driver.vehicle_type)#total passengers filtered in html
    driver_special_request = driver.special_request
    return render(request,'account/view_open_ride.html',{'all_ride':all_ride,'driver_max_capacity':driver.max_number_passengers,'user':user,'driver_special_request':driver_special_request})

def confirm_ride(request,id):
    driver = Driver.objects.get(user=request.user)
    try:
        confirmed_ride = Ride.objects.get(id=id)
    except Ride.DoesNotExist:
        return render(request, 'account/error_message.html',{'user':request.user})

    if confirmed_ride.total_people> driver.max_number_passengers:
        return render(request,'account/error_message.html',{'user':request.user})
    if confirmed_ride.special_request != '' and confirmed_ride.special_request != driver.special_request:
        return render(request, 'account/error_message.html',{'user':request.user})
    confirmed_ride.status='Confirmed'
    confirmed_ride.driver=driver
    confirmed_ride.save()

    subject = '[Riding Share Service] Your Order has been confirmed'
    send_message = f'Thanks for using our service, Your driver: {driver.user.first_name} {driver.user.last_name} is approaching.'
    email_from= settings.EMAIL_HOST_USER
    email_list = []
    for share in confirmed_ride.sharer.all():
        email = share.user.email
        email_list.append(email)
    send_mail(subject,send_message,email_from,email_list)

    email_list = [confirmed_ride.owner.email,]
    send_mail(subject,send_message,email_from,email_list)
    
    send_message = f'Thanks for using our service, Mr/Dr: {driver.user.first_name} {driver.user.last_name}, you order has been confirmed successfully.'
    email_list = [driver.user.email,]
    send_mail(subject,send_message,email_from,email_list)
    
    return redirect('driversearch',id=request.user.id)

def complete_ride(request,id):
    completed_ride = Ride.objects.get(id=id)
    completed_ride.status='Completed'
    #Update corresponding joined sharer's myUser info
    for sharer in completed_ride.sharer.all():
        sharer.total_sharers=None
        sharer.save()
    completed_ride.save()
    return redirect('view_drive_ride',id=request.user.id)

def view_drive_ride(request,id):
    driver = Driver.objects.get(user=request.user)
    all_ride = Ride.objects.all().filter(driver= driver)
    if request.method == 'POST':
        confirmed_or_completed = request.POST['confirmed_or_completed']
        if confirmed_or_completed == "Confirmed":
            all_ride = Ride.objects.all().filter(driver= driver, status='Confirmed')
        elif confirmed_or_completed == "Completed":
            all_ride = Ride.objects.all().filter(driver= driver, status='Completed')
        else:
            return redirect('view_drive_ride',id=id)
    return render(request,'account/view_drive_ride.html',{'all_ride':all_ride,'user':request.user})


######################################################################################
# SHARER
######################################################################################
def join_ride(request,id):
    user = User.objects.get(id=id)
    form = SharerRequestForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            destination = form.cleaned_data['destination']
            earliest = form.cleaned_data['earliest']
            latest = form.cleaned_data['latest']
            number_of_sharers = form.cleaned_data['number_of_passengers']

            #UPDATE MYUSER TOTAL_SHARERS
            my_user = myUser.objects.get(user=user)
            my_user.total_sharers = number_of_sharers
            my_user.save()
            
            all_ride_include_joined = Ride.objects.filter(destination=destination,shared_or_not=True)
            ride_have_joined = my_user.ride_set.all()
            all_ride = all_ride_include_joined.exclude(id__in=ride_have_joined)
            return render(request,'account/view_available_ride.html',{'all_ride':all_ride,'destination':destination,'earliest':earliest,'latest':latest,'number_of_sharers_temp':number_of_sharers,'user':user})
    
    return render(request,'account/sharer_request.html',{'form':form})

def join_this_ride(request,id): 
    user = request.user
    my_user = myUser.objects.get(user=user)
    joined_ride = Ride.objects.get(id=id)
    joined_ride.sharer.add(my_user)
    #UPDATE TOTAL PEOPLE IN RIDE
    joined_ride.total_people += my_user.total_sharers
    joined_ride.save()
    return redirect('view_shared_ride',user.id)



def view_shared_ride(request,id):
    my_user = myUser.objects.get(user = request.user)
    all_ride = my_user.ride_set.all()
    status = 'All'
    if request.method == 'POST':
        confirmed_or_completed = request.POST['confirmed_or_completed']
        if confirmed_or_completed == "Confirmed":
            status='Confirmed'
            all_ride = my_user.ride_set.all().filter(status='Confirmed')
        elif confirmed_or_completed == "Completed":
            status='Completed'
            all_ride = my_user.ride_set.all().filter(status='Completed')
        else:
            return redirect('view_shared_ride',id=id)
    return render(request,'account/view_share_ride.html',{'all_ride':all_ride,'user':request.user,'status':status})

def quit_this_ride(request,id):
    this_ride = Ride.objects.get(id=id)
    my_user = myUser.objects.get(user=request.user)
    if this_ride.status == 'Confirmed':
        return render(request, 'account/error_message.html',{'user':request.user})
    
    this_ride.sharer.remove(my_user)
    this_ride.total_people-= my_user.total_sharers
    this_ride.save()
    
    #UPDATE MYUSER TOTAL_SHARES
    my_user.total_sharers = None
    my_user.save()
    
    return redirect('view_shared_ride',request.user.id)
