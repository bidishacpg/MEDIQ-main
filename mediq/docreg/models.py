from django.db import models
from tinymce.models import HTMLField
class Docreg(models.Model):
    id = models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField()
    languages=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    contactNumber=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    medicalDegree=models.CharField(max_length=50)
    licenseNumber=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    workplace=models.CharField(max_length=50)
    workAddress=models.CharField(max_length=50)
    workContact=models.CharField(max_length=50)
    workEmail=models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    photo = models.ImageField(upload_to='media/',max_length=250,null=True,default=None)

    monday_start = models.TimeField(null=True, blank=True)
    monday_end = models.TimeField(null=True, blank=True)
    tuesday_start = models.TimeField(null=True, blank=True)
    tuesday_end = models.TimeField(null=True, blank=True)
    wednesday_start = models.TimeField(null=True, blank=True)
    wednesday_end = models.TimeField(null=True, blank=True)
    thursday_start = models.TimeField(null=True, blank=True)
    thursday_end = models.TimeField(null=True, blank=True)
    friday_start = models.TimeField(null=True, blank=True)
    friday_end = models.TimeField(null=True, blank=True)
    saturday_start = models.TimeField(null=True, blank=True)
    saturday_end = models.TimeField(null=True, blank=True)
    sunday_start = models.TimeField(null=True, blank=True)
    sunday_end = models.TimeField(null=True, blank=True)


    