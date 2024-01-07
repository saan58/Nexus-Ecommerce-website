from django.shortcuts import render,HttpResponse,redirect 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("User logged in successfully")
            return redirect('home')
        else:
            print("Authentication failed")
    return render(request,'login.html')  

# def logout(request):
#     logout(request)
#     return render(request,'index.html')
   
def signUp(request):
    if request.method=="POST":
        username=request.POST['username']
        # first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        signUp=User.objects.create_user(email=email,username=username,password=password)
        signUp.save()
        messages.success(request,"Account created!!")
        return redirect('login')
    return render(request,'signUp.html')

def men(request):
    return render(request,'men.html')

def women(request):
    return render(request,'women.html')

def kids(request):
    return render(request,'kids.html')

def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        textbox=request.POST.get('textbox')
        other_details=request.POST.get('other_details')
        contact=Contact(email=email,name=name,textbox=textbox,other_details=other_details,date=datetime.today())
        contact.save()
        messages.success(request,"Successfully submitted. Our team will contact you via email shortly.")
    return render(request,'contact.html')