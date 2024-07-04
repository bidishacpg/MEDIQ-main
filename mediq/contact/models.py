from django.db import models
from tinymce.models import HTMLField
class Contact(models.Model):
    username=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='contac/',null=True,default=None)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    feedback=models.CharField(max_length=200)
