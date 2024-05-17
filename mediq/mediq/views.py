from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def patreg(request):
    return render(request,"patregister.html")
    