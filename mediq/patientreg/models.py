from django.db import models
from tinymce.models import HTMLField
class Patientreg(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    message=models.TextField()
    phone=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='patient/',max_length=250,null=True,default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
