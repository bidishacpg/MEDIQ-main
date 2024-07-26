
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from hospreg.forms import hospregisterr, hosploginn
from docreg.forms import docregisterr, docloginn
from patientreg.forms import patregisterr, patloginn
from Book.models import Book
from contact.models import Contact
from contact.forms import Contactform
from patientreg.models import Patientreg
from docreg.models import Docreg
from hospreg.models import Hospreg
import logging
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def home(request):
    hosplist = Hospreg.objects.all()
    doclist = Docreg.objects.all()  
    hospital_count = Hospreg.objects.count()
    doctor_count = Docreg.objects.count()
    patient_count = Patientreg.objects.count()# Fetch all doctors
    contactlist = Contact.objects.all()
    
    if request.method == "GET":
        jb = request.GET.get('hospname')
        if jb is not None:
            hosplist = Hospreg.objects.filter(hospital_name__icontains=jb)
    
    context = {
        'hosplist': hosplist,
        'doclist': doclist,
           'hospital_count': hospital_count,
        'doctor_count': doctor_count,
        'patient_count': patient_count,  # Add doctors to the context
        'contactlist':contactlist
    }
    
    return render(request, "index.html", context)
logger = logging.getLogger(__name__)

def book(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        hospital_id = request.POST.get('hospital')
        doctor_id = request.POST.get('doctor')
        date= request.POST.get('date')
        message = request.POST.get('message')
        phone = request.POST.get('phone')

        # Fetch hospital and doctor objects
        hospital = Hospreg.objects.get(id=hospital_id)
        doctor = Docreg.objects.get(id=doctor_id)

        booking_count = Book.objects.filter(date=date,hospital=hospital).count()
        if booking_count >= 5:
            return HttpResponse("Sorry, the maximum number of bookings for this date has been reached. Please select another date.")
        
        

        # Save the booking to the database
        en = Book(first_name=first_name, last_name=last_name, age=age, email=email, phone=phone, message=message, gender=gender, hospital=hospital, doctor=doctor, date=date)
        en.save()

    # Pass hospitals and doctors to the form template
    hospitals = Hospreg.objects.all()
    doctors = Docreg.objects.all()

    return render(request, 'appoint.html', {'hospitals': hospitals, 'doctors': doctors})

def docreg(request):
    if request.method == 'POST':
        print("Received POST request")
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        form = docregisterr(request.POST, request.FILES) 
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('doclogin')
        else:
            # Print form errors to the console
            print("Form is not valid")
            print(form.errors)
            hospitals = Hospreg.objects.all()  
            return render(request, 'docregister.html', {'form': form, 'hospitals': hospitals})
    else:
        form = docregisterr()
        hospitals = Hospreg.objects.all()
    return render(request, 'docregister.html', {'form': form, 'hospitals': hospitals})


def doclist(request):
    doclist=Docreg.objects.all()

    dat={
        'doclist':doclist
    }
    return render(request,"doclist.html",dat)

def doclogin(request):
    error_message = None
    if request.method == 'POST':
        form = docloginn(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                docreg = Docreg.objects.get(email=email, password=password)
                request.session['docreg_id'] = docreg.id
                request.session['docreg_email'] = docreg.email
                return redirect('dochome')  # Redirect to a success page
            except Docreg.DoesNotExist:
                error_message = 'Invalid username or password (please provide unique email address)'
    else:
        form = docloginn()
    return render(request, 'doclogin.html', {'form': form, 'error_message': error_message})
 
def doclogout(request):
    try:
        del request.session['docreg_id']
        del request.session['docreg_email']
    except KeyError:
        pass
    return redirect('doclogin')

#subject='testing mail'
#form_emails='bidishachapagai@gmail.com'
#msg='<p>you have succesfully registered</p>'
#to='ichhashah4681@gmail.com'
#msg=EmailMultiAlternatives(subject,msg,form_emails,[to])
#msg.content_subtype='html'
#msg.send()

def patreg(request):
    if request.method == 'POST':
        print("Received POST request")
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        form = patregisterr(request.POST, request.FILES)  # Including request.FILES for file uploads
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('patlogin')
        else:
            # Print form errors to the console
            print("Form is not valid")
            print(form.errors)
            return render(request, 'patregister.html', {'form': form})
    else:
        form = patregisterr()
        return render(request, 'patregister.html', {'form': form})

def doctorprofile(request,id):
    # Fetch the specific doctor from the database using the primary key (doc_id)
    doclist = Docreg.objects.get(id=id)
    data={
        'doclist':doclist
    }
    return render(request, 'doctorprofile.html',data)

def hospage(request, id):
    hosplist = Hospreg.objects.get(id=id)
    doctors = Docreg.objects.filter(workplace=hosplist.hospital_name)  # Filter doctors by workplace
    data = {
        'hosplist': hosplist,
        'doctors': doctors
    }
    return render(request, 'hospage.html', data)

def patlogin(request):
    error_message = None
    if request.method == 'POST':
        form = patloginn(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                patientreg = Patientreg.objects.get(email=email, password=password)
                request.session['patientreg_id'] = patientreg.id
                request.session['patientreg_email'] = patientreg.email
                return redirect('pathome')  # Redirect to a success page
            except Patientreg.DoesNotExist:
                error_message = 'Invalid username or password'
    else:
        form = patloginn()
    return render(request, 'patlogin.html', {'form': form, 'error_message': error_message})

def patlogout(request):
    try:
        del request.session['patientreg_id']
        del request.session['patient_email']
    except KeyError:
        pass
    return redirect('patlogin')

    
def hospreg(request):
    if request.method == 'POST':
        print("Received POST request")
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        form = hospregisterr(request.POST, request.FILES)  # Including request.FILES for file uploads
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('hosplogin')
        else:
            # Print form errors to the console
            print("Form is not valid")
            print(form.errors)
            return render(request, 'hospregister.html', {'form': form})
    else:
        form = hospregisterr()
        return render(request, 'hospregister.html', {'form': form})


def hosplogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            hospreg = Hospreg.objects.get(email=email, password=password)
            request.session['hospreg_id'] = hospreg.id
            request.session['hospreg_email'] = hospreg.email
            return redirect('hosphome')  # Redirect to a success page
        except Hospreg.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    return render(request, 'hosplogin.html')

def hosplogout(request):
    try:
        del request.session['hospreg_id']
        del request.session['hospreg_email']
    except KeyError:
        pass
    return redirect('hosplogin')

def ambulance(request):
    return render(request,"ambulance.html")
 
def hosplist(request):
    hosplist=Hospreg.objects.all()

    dat={
        'hosplist':hosplist
    }
    return render(request,"hosplist.html",dat)

def aboutus(request):
    return render(request,"aboutus.html")

def services(request):
    return render(request,"services.html")

def pathome(request):
    hosplist = Hospreg.objects.all()
    doclist = Docreg.objects.all() 
    hospital_count = Hospreg.objects.count()
    doctor_count = Docreg.objects.count()
    patient_count = Patientreg.objects.count()# Fetch all doctors
    contactlist = Contact.objects.all()

    if request.method == "GET":
        jb = request.GET.get('hospname')
        if jb is not None:
            hosplist = Hospreg.objects.filter(hospital_name__icontains=jb)
    
    context = {
        'hosplist': hosplist,
        'doclist': doclist,
         'hospital_count': hospital_count,
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'contactlist':contactlist
    }
    return render(request,"pathome.html",context)
@login_required
def dochome(request):
    docreg_id = request.session.get('docreg_id')
    
    # Retrieve data relevant to the logged-in hospital
    doclist = Docreg.objects.filter(id=docreg_id)
    bookings = Book.objects.filter(doctor__in=[doc.fullname for doc in doclist])
    return render(request,"dochome.html",{'doclist': doclist, 'bookings': bookings})

@login_required
def hosphome(request):
    # Retrieve hospital registration details from session
    hospreg_id = request.session.get('hospreg_id')
    
    # Retrieve data relevant to the logged-in hospital
    hosplist = Hospreg.objects.filter(id=hospreg_id)
    bookings = Book.objects.filter(hospital__in=[hosp.hospital_name for hosp in hosplist])
    doctors = Docreg.objects.filter(workplace__in=[hosp.hospital_name for hosp in hosplist])
    # Pass the hospital data to the template for rendering
    return render(request, 'hosphome.html', {'hosplist': hosplist, 'bookings': bookings,'doctors':doctors})

def confirm_appointment(request, booking_id):
    # Get the booking object
    booking = get_object_or_404(Book, id=booking_id)
    booking.confirmed = True
    booking.save()
    try:
            send_mail(
                'Appointment Confirmed',
                f'Your booking for hospital {booking.hospital} with Dr. {booking.doctor} is confirmed.',
                'chapagaibidisha@gmail.com',  # From email
                [booking.email],  # To email (user's email from the form)
                fail_silently=False,
            )
    except Exception as e:
            logger.error(f"Error sending email: {e}")
    # Perform actions related to confirmation (e.g., send email)
    # Assuming confirmation is successful, you can redirect to the same page or any other page
    # For now, let's redirect to the same page
    # Perform actions related to confirmation (e.g., send email)
    # Assuming confirmation is successful, you can redirect to the same page or any other page
    # For now, let's redirect to the same page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_appointment(request, booking_id):
    # Get the booking object
    booking = get_object_or_404(Book, id=booking_id)
    # Perform deletion
    booking.delete()
    try:
            send_mail(
                'Appointment Deleted',
                f'Sorry Your booking for hospital {booking.hospital} with Dr. {booking.doctor} is deleted due to technical errors.',
                'chapagaibidisha@gmail.com',  # From email
                [booking.email],  # To email (user's email from the form)
                fail_silently=False,
            )
    except Exception as e:
            logger.error(f"Error sending email: {e}")
    # Redirect to the same page or any other page after deletion
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST, request.FILES)  # Don't forget request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('contact')  # Redirect to a success page
    else:
        form = Contactform()
    
    return render(request, 'contact.html', {'form': form})
     