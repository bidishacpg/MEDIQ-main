from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

<<<<<<< HEAD
def doclogin(request):
    return render(request,"doclogin.html")
=======
def docreg(request):
    return render(request,"docregister.html")
def patreg(request):
    return render(request,"patregister.html")
    
>>>>>>> 4cd2ae36c7fefb81c73acdd43f7aab78ddf5a894
