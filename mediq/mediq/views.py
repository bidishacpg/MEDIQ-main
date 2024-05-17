from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

<<<<<<< HEAD
def register(request):
    return render(request,"docregister.html")
=======
def patreg(request):
    return render(request,"patregister.html")
    
>>>>>>> bed156a5d7de685b0fd40773851214dda9f38cfc
