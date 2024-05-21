from django.db import models
from tinymce.models import HTMLField
class Hospreg(models.Model):
    hospital_name=models.CharField(max_length=50)
    hospital_type=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    license=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='hosp/',null=True,default=None)
