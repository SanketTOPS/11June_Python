from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def getall(request):
    stdata=userdata.objects.all()
    serial=userserial(stdata,many=True)
    return Response(data=serial.data)
    
    
    