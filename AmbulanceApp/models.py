from django.db import models


# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Ambulance(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    AMBULANCE_TYPE = [
        ('Basic Life Support Ambulance', 'Basic Life Support Ambulance'),
        ('Advance Life Support Ambulance', 'Advance Life Support Ambulance'),
        ('Patient Transfer Ambulance', 'Patient Transfer Ambulance'),
        ('Mortuary Ambulance', 'Mortuary Ambulance'),
    ]
    STATUS = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    Ambulance_No = models.CharField(max_length=14)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    Ambulance_type = models.CharField(max_length=50, choices=AMBULANCE_TYPE)
    Status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.firstname + " " + self.lastname

