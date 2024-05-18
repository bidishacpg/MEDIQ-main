from django.db import models
from tinymce.models import HTMLField
class Docreg(models.Model):
    fullname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField()
    languages=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    contactNumber=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    medicalDegree=models.CharField(max_length=50)
    licenseNumber=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    workplace=models.CharField(max_length=50)
    workAddress=models.CharField(max_length=50)
    workContact=models.CharField(max_length=50)
    workEmail=models.CharField(max_length=50)
