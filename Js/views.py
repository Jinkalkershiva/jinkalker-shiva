from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import Authantication,Autrorization
from django.contrib import HttpResponse,HttpResponseRedirect


def login(request):
    return render(request,"login.html")

def dashboard(request):
    return render(request,'dashboard.html')
def signup(request):
    return render(request,'signup.html')
def Aboutus(request):
    return render(request,'Aboutus.html')


