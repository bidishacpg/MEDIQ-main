
from django.http import HttpResponse
from django.shortcuts import render,redirect
#from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from Book.models import Book
from patientreg.models import Patientreg
from docreg.models import Docreg
from hospreg.models import Hospreg


def home(request):
    hosplist=Hospreg.objects.all()

    dat={
        'hosplist':hosplist
    }
    return render(request,"index.html",dat)

def book(request):
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
      en= Book(first_name=first_name, last_name=last_name, age=age, email=email, phone=phone, message=message, gender=gender, hospital=hospital , doctor=doctor )
      en.save()
     return render(request,'appoint.html')

def docreg(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        nationality = request.POST.get('nationality')
        languages = request.POST.get('languages')
        contactNumber = request.POST.get('contactNumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        medicalDegree = request.POST.get('medicalDegree')
        licenseNumber = request.POST.get('licenseNumber')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        workplace = request.POST.get('workplace')
        workAddress = request.POST.get('workAddress')
        workContact = request.POST.get('workContact')
        workEmail = request.POST.get('workEmail')
        photo = request.FILES.get('photo')

        def get_time_field(field_name):
            field_value = request.POST.get(field_name)
            return field_value if field_value else None
        
        monday_start = get_time_field('monday_start')
        monday_end = get_time_field('monday_end')
        tuesday_start = get_time_field('tuesday_start')
        tuesday_end = get_time_field('tuesday_end')
        wednesday_start = get_time_field('wednesday_start')
        wednesday_end = get_time_field('wednesday_end')
        thursday_start = get_time_field('thursday_start')
        thursday_end = get_time_field('thursday_end')
        friday_start = get_time_field('friday_start')
        friday_end = get_time_field('friday_end')
        saturday_start = get_time_field('saturday_start')
        saturday_end = get_time_field('saturday_end')
        sunday_start = get_time_field('sunday_start')
        sunday_end = get_time_field('sunday_end')

        en = Docreg(
            fullname=fullname, gender=gender, dob=dob, languages=languages, nationality=nationality,
            contactNumber=contactNumber, email=email, password=password, medicalDegree=medicalDegree,
            licenseNumber=licenseNumber, specialization=specialization, experience=experience,
            workplace=workplace, workAddress=workAddress, workContact=workContact, workEmail=workEmail,
            photo=photo,monday_start=monday_start,
            monday_end=monday_end, tuesday_start=tuesday_start,
            tuesday_end=tuesday_end, wednesday_start=wednesday_start,
            wednesday_end=wednesday_end, thursday_start=thursday_start,
            thursday_end=thursday_end, friday_start=friday_start,
            friday_end=friday_end, saturday_start=saturday_start,
            saturday_end=saturday_end, sunday_start=sunday_start,
            sunday_end=sunday_end
        )

        en.save()
        return redirect('/doclogin')  # Redirect to login page after successful registration

    return render(request, "docregister.html")

def doclist(request):
    doclist=Docreg.objects.all()

    dat={
        'doclist':doclist
    }
    return render(request,"doclist.html",dat)

def doclogin(request):
     
     return render(request, "doclogin.html")

#subject='testing mail'
#form_emails='bidishachapagai@gmail.com'
#msg='<p>you have succesfully registered</p>'
#to='ichhashah4681@gmail.com'
#msg=EmailMultiAlternatives(subject,msg,form_emails,[to])
#msg.content_subtype='html'
#msg.send()

def patreg(request):
    if request.method=="POST":
      first_name =request.POST.get('first_name')
      last_name =request.POST.get('last_name')
      age =request.POST.get('age')
      email=request.POST.get('email')
      gender =request.POST.get('gender')
      password =request.POST.get('password')
      address =request.POST.get('address')
      message =request.POST.get('message')
      phone =request.POST.get('phone')
      photo = request.FILES.get('photo') 
      

      en= Patientreg(first_name=first_name, last_name=last_name, age=age, email=email, phone=phone, message=message, gender=gender, password=password , address=address,photo=photo )
      en.save()
    return render(request,"patregister.html")


def hospreg(request):
   
    if request.method == "POST":
        hospital_name = request.POST.get('hospital_name')
        hospital_type = request.POST.get('hospital_type')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        license = request.POST.get('license')
        city = request.POST.get('city')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        photo = request.FILES.get('photo') 

        en = Hospreg(
            hospital_name=hospital_name,
            hospital_type=hospital_type,
            license=license,
            email=email,
            phone=phone,
            city=city,
            password=password,
            confirm_password=confirm_password,
            address=address,
            photo=photo
        )
        en.save()

    return render(request, 'hospregister.html')

def hosplogin(request):
    return render(request,"hosplogin.html")

def hospage(request):
    return render(request,"hospage.html")
 
def hosplist(request):
    hosplist=Hospreg.objects.all()

    dat={
        'hosplist':hosplist
    }
    return render(request,"hosplist.html",dat)

def contact(request):
    return render(request,"contact.html")
def aboutus(request):
    return render(request,"aboutus.html")

def services(request):
    return render(request,"services.html")



