from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

<<<<<<< HEAD
=======
<<<<<<< HEAD
def book(request):
    return render(request,'appoint.html')
=======
<<<<<<< HEAD
>>>>>>> 0ee13d0627cb5f07a91306d0d790027f70f4e887
def doclogin(request):
    return render(request,"doclogin.html")
def docreg(request):
    return render(request,"docregister.html")
def patreg(request):
    return render(request,"patregister.html")
    
<<<<<<< HEAD
=======
>>>>>>> 4cd2ae36c7fefb81c73acdd43f7aab78ddf5a894
>>>>>>> e7cc38101d743837789281a35540a985e617608e
>>>>>>> 0ee13d0627cb5f07a91306d0d790027f70f4e887
