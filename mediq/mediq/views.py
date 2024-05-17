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

