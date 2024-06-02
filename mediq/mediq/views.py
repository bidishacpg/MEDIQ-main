
from django.http import HttpResponse
from django.shortcuts import render,redirect
from hospreg.forms import hospregisterr, hosploginn
from docreg.forms import docregisterr, docloginn
from patientreg.forms import patregisterr, patloginn
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
            return render(request, 'docregister.html', {'form': form})
    else:
        form = docregisterr()
    return render(request, 'docregister.html', {'form': form})


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
                return redirect('aboutus')  # Redirect to a success page
            except :
                error_message = 'Invalid username or password'
     else:
        form = docloginn()
     return render(request, 'doclogin.html', {'form': form, 'error_message': error_message})


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

def hospage(request,id):
    hosplist = Hospreg.objects.get(id=id)
    data={
        'hosplist':hosplist
    }
    return render(request, 'hospage.html',data)
      # Assuming you have only one hospita

def patlogin(request):
    error_message = None
    if request.method == 'POST':
        form = patloginn(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                patientreg = Patientreg.objects.get(email=email, password=password)
                return redirect('aboutus')  # Redirect to a success page
            except :
                error_message = 'Invalid username or password'
    else:
        form = patloginn()
    return render(request, 'patlogin.html', {'form': form, 'error_message': error_message})

    
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
    error_message = None
    if request.method == 'POST':
        form = hosploginn(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                hospreg = Hospreg.objects.get(email=email, password=password)
                return redirect('aboutus')  # Redirect to a success page
            except :
                error_message = 'Invalid username or password'
    else:
        form = hosploginn()
    return render(request, 'hosplogin.html', {'form': form, 'error_message': error_message})


def ambulance(request):
    return render(request,"ambulance.html")
 
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



