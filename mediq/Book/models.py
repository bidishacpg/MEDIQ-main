from django.db import models
from tinymce.models import HTMLField
class Book(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    hospital=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    date = models.DateField()
    message=models.TextField()
    phone=models.CharField(max_length=50)