from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=30, null=True)
    family = models.CharField(max_length=30, null=True)
    nationalId = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=50, null=True)
        
class manager(models.Model):
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=30, null=True)
    family = models.CharField(max_length=30, null=True)

class Room(models.Model):
    no = models.IntegerField(null=True)
    capacity = models.IntegerField(null=True)
    isIdle = models.BooleanField(null=True)
    ecoclass = models.IntegerField(null=True)
    beds = models.IntegerField(null=True) 


class Reservation(models.Model):
    startDate = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    endDate = models.DateField(null=True)
    endTime = models.TimeField(null=True)
    isActive = models.BooleanField(default=False)
    score = models.IntegerField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True) 