
from django.db import models
from django.contrib.auth.models import User

class myUser(models.Model):#If User created, myUser created
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_driver = models.BooleanField(default = False)
    total_sharers = models.IntegerField(null=True)

class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #is_driver = models.BooleanField(default = True)
    TYPE = [('Economy', 'Economy' ),
            ('Intermediate', 'Intermediate'),
            ('Standard', 'Standard'),
            ('Premium','Premium')]
    vehicle_type = models.CharField(max_length=20, choices= TYPE,null=True)
    license_plate_number = models.CharField(max_length=200,null=True)
    max_number_passengers = models.IntegerField(null=True)
    special_request = models.CharField(max_length=200, blank =True,null=True)
class Ride(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)#related_name = 'owner'
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    sharer = models.ManyToManyField(myUser,blank=True)
    shared_or_not = models.BooleanField(default = False)
    destination = models.CharField(max_length = 60, blank=False)
    arrival_time = models.DateTimeField(null=True)
    TYPE_vehicle = [('Economy', 'Economy' ),
            ('Intermediate', 'Intermediate'),
            ('Standard', 'Standard'),
            ('Premium','Premium')]
    vehicle_type = models.CharField(max_length=20, choices= TYPE_vehicle,null=True)

    TYPE_status=[
        ('Open','Open'),
        ('Confirmed','Confirmed'),
        ('Completed','Completed')
    ]
    status = models.CharField(max_length = 20, choices = TYPE_status, null = True, default = 'Open')
    is_reached = models.BooleanField(default = False)
    total_passengers = models.IntegerField(null = True)
    total_people = models.IntegerField(null=True)
    sharer_number = models.IntegerField(null = True)
    special_request = models.CharField(max_length=20, blank = True, default='')
    
