from django.db import models

from django.template.defaultfilters import date
# Create your models 
from django.utils import timezone ,dateformat
formatted_date = dateformat.format(timezone.now(), 'Y-m-d')
# Create your models here.

class Patient(models.Model):
    CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other')
        )
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Gender=models.CharField(max_length=100,choices=CHOICE)
    Age = models.PositiveIntegerField()
    Disease = models.CharField(max_length=200)
    Doctor_name = models.CharField(max_length=100)
    Doctor_Fees = models.PositiveIntegerField(default=500)
    date=models.DateField()
    time=models.TimeField()



