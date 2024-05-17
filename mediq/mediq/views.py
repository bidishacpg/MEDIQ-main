from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def book(request):
    return render(request,'appoint.html')

def doclogin(request):
    return render(request,"doclogin.html")

def docreg(request):
    return render(request,"docregister.html")

def patreg(request):
    return render(request,"patregister.html")
<<<<<<< HEAD




    
=======
    

>>>>>>> 2d6174f9a9c4eb37279effd4e24378867276ac1c
