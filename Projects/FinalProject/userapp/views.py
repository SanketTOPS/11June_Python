from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
import random
from django.core.mail import send_mail
from FinalProject import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    msg=""
    if request.method=='POST':
        email=request.POST['email']
        pas=request.POST['password']
        
        user=Usersignup.objects.filter(email=email,password=pas)
        if user: #TRUE
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session["user"]=email
            return redirect('/')
        else:
            print("Error!Login Faild...")
            msg="Error!Login Faild..."
    return render(request,'login.html',{'msg':msg})

otp=0
def signup(request):
    msg=""
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Signup Successfully!"
            
            # OTP Sending Code
            global otp
            otp=random.randint(111111,999999)
            
            sub="Your One Time Password!"
            message=f"Dear User!\n\nThanks for register our service!\n\For account verification, Your one time password is {otp}.\n\nThanks & Regards\nNotesApp Team\n+91 9724799469 | sanket.tops@gmail.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST["email"]]
            
            send_mail(subject=sub,message=message,from_email=from_email,recipient_list=to_email)
            
            print("Email sent successfully!")
            return redirect('otpverify')
        else:
            print(form.errors)
            msg="Error!Something went wrong..."
    return render(request,'signup.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('login')

def otpverify(request):
    global otp
    print(otp)
    if request.method=='POST':
        myotp=request.POST['otp']
        if otp==int(myotp):
            print("Signup Successfully!")
            return redirect("login")
        else:
            print("Error!OTP Verification faild...Try again!")
    return render(request,'otpverify.html')