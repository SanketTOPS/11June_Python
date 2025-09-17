from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'register.html')