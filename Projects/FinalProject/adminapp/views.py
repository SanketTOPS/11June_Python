from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from datetime import datetime
from django.core.mail import send_mail
from FinalProject import settings

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

def notes_approve(request,id):
    note=get_object_or_404(Notes,id=id)
    note.status="Approve"
    note.updated_at=datetime.now()
    note.save()
    print("Notes Approved by Admin!")
    
    #Email Sending Code
    sub="Notes Approved!"
    msg=f"Dear User\n\nCongratulation!\n\nYour notes has been approved by Admin!.\nThanks for using our service.\n\nThanks & Regards\nNotesApp Team\n+91 9724799469 | sanket.tops@gmail.com"
    from_id=settings.EMAIL_HOST_USER
    to_id=[note.email.email]
    
    send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
    
    print(note.email.email)
    return redirect("admin_notesdata")
    

def notes_reject(request,id):
    note=get_object_or_404(Notes,id=id)
    note.status="Reject"
    note.updated_at=datetime.now()
    note.save()
    print("Notes Rejected by Admin!")
    return redirect("admin_notesdata")