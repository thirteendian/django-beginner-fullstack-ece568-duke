
from django.db import models
from django.contrib.auth.models import User

class myUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_driver = models.BooleanField(default = False)

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
