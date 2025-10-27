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
    try:
        user=request.session.get("user")
        email=Usersignup.objects.get(email=user)
        if request.method=='POST':
            form=NotesForm(request.POST,request.FILES)
            if form.is_valid():
                temp=form.save(commit=False)
                temp.status="Pending"
                temp.email=email
                temp.save()
                print("Notes Submitted!")
                return redirect('/')
            else:
                print(form.errors)
    except:
        print("Error!")    
    return render(request,'notes.html',{'user':user})

def profile(request):
    userid=request.session.get("userid")
    cuser=Usersignup.objects.get(id=userid)
    if request.method=='POST':
        form=SignupForm(request.POST,instance=cuser)
        if form.is_valid():
            form.save()
            msg="Update Successfully!"
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'profile.html',{'userid':cuser})

def about(request):
    user=request.session.get("user")
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get("user")
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Message sent successfully!")
            #Email Sending
            sub="Thank You!"
            msg=f"Dear User\n\nThanks for connecting with us, and also using our services.\n\nWe will contact you shortly.\n\nThanks & Regards\nNotesApp Team\n+91 9724799469 | sanket.tops@gmail.com"
            from_mail=settings.EMAIL_HOST_USER
            to_mail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
            
            return redirect('contact')
        else:
            print(form.errors)
    return render(request,'contact.html',{'user':user})

def login(request):
    msg=""
    if request.method=='POST':
        email=request.POST['email']
        pas=request.POST['password']
        
        user=Usersignup.objects.filter(email=email,password=pas)
        userid=Usersignup.objects.get(email=email)
        print(userid.id)
        if user: #TRUE
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session["user"]=email
            request.session["userid"]=userid.id
            
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
        em=request.POST["email"]
        email=Usersignup.objects.filter(email=em).exists()
        if email:
            print("Email addredd is already exists!")
            msg="Email addredd is already exists!"
        else:
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