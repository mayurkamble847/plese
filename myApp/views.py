from django.shortcuts import render,HttpResponse
from myApp.models import Contact

# Create your views here.
def  index(request):
    context={
        'var1':'Hello guys!!! channel to my welcome.',
        'var2':'Hello channel welcome to my guys'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html') 
    

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
       Name=request.POST.get('name')
       Email=request.POST.get('email')
       Phone=request.POST.get('phone')
       Desc=request.POST.get('desc')
       print(Name,Email,Phone,Desc)
       contact=Contact(name=Name,email=Email,phone=Phone,desc=Desc)
       contact.save()
    return render(request,'contact.html')