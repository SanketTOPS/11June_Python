from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

@api_view(["GET"])
def getall(request):
    stdata=userdata.objects.all()
    serial=userserial(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=userdata.objects.get(id=id)
    except userdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=userserial(stid)
    return Response(data=serial.data)
        
@api_view(['GET','DELETE'])
def deletedata(request,id):
    try:
        stid=userdata.objects.get(id=id)
    except userdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=userserial(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        userdata.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
        
@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=userserial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stid=userdata.objects.get(id=id)
    except userdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=userserial(stid)
        return Response(data=serial.data)
    if request.method=='PUT':
        serial=userserial(data=request.data,instance=stid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
        
def home(request):
    url="http://127.0.0.1:8000/getall/"
    req=requests.get(url)
    data=req.json()
    #print(data)
    return render(requests,'home.html',{'data':data})
    

    
    
    