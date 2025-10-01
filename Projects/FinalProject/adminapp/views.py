from django.shortcuts import render,redirect
from userapp.models import *

# Create your views here.
def admin_login(request):
    if request.method=='POST':
        if request.POST["username"]=="admin" and request.POST["password"]=="tops@123":
            print("Login Successfull!")
            return redirect("admin_dashboard")
        else:
            print("Error!Login Faild...")
    return render(request,'admin_login.html')


def admin_dashboard(request):
    userdata=Usersignup.objects.all()
    u=len(userdata)
    notesdata=Notes.objects.all()
    n=len(notesdata)
    return render(request,'admin_dashboard.html',{'u':u,'n':n,'userdata':userdata})

def admin_userdata(request):
    userdata=Usersignup.objects.all()
    return render(request,'admin_userdata.html',{'userdata':userdata})

def admin_notesdata(request):
    notesdata=Notes.objects.all()
    return render(request,'admin_notesdata.html',{'notesdata':notesdata})