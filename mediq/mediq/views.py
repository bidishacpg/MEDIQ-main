from django.http import HttpResponse
from django.shortcuts import render,redirect
from patientreg.models import Patientreg
from docreg.models import Docreg

def home(request):
    return render(request,"index.html")

def book(request):
    return render(request,'appoint.html')

def doclogin(request):
    return render(request,"doclogin.html")

def docreg(request):
    if request.method=="POST":
      fullname =request.POST.get('fullname')
      gender =request.POST.get('gender')
      dob =request.POST.get('dob')
      nationality=request.POST.get('nationality')
      languages=request.POST.get('languages')
      contactNumber =request.POST.get('contactNumber')
      email =request.POST.get('email')
      medicalDegree =request.POST.get('medicalDegree')
      licenseNumber =request.POST.get('licenseNumber')
      specialization =request.POST.get('specialization')
      experience =request.POST.get('experience')
      workplace =request.POST.get('workplace')
      workAddress =request.POST.get('workAddress')
      workContact =request.POST.get('workContact')
      workEmail =request.POST.get('workEmail')
      

      en= Docreg(fullname=fullname,
                gender=gender,
                dob=dob,
                languages=languages,
                nationality=nationality,
                contactNumber=contactNumber,
                email=email,
                medicalDegree=medicalDegree,
                licenseNumber=licenseNumber,
                specialization=specialization,
                experience=experience,
                workplace=workplace,
                workAddress=workAddress,
                workContact=workContact,
                workEmail=workEmail )
      en.save()
    return render(request, "docregister.html")

def patreg(request):
    if request.method=="POST":
      first_name =request.POST.get('first_name')
      last_name =request.POST.get('last_name')
      age =request.POST.get('age')
      email=request.POST.get('email')
      gender =request.POST.get('gender')
      hospital =request.POST.get('hospital')
      doctor =request.POST.get('doctor')
      message =request.POST.get('message')
      phone =request.POST.get('phone')
      

      en= Patientreg(first_name=first_name, last_name=last_name, age=age, email=email, phone=phone, message=message, gender=gender, hospital=hospital , doctor=doctor )
      en.save()
    return render(request,"patregister.html")


def hospreg(request):
    return render(request,'hospregister.html')
