from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Home(request):
    return render(request,"home.html",{})

def Register(request):
    if request.method=="POST":
        User_register.objects.create(name=request.POST["name"],email=request.POST["email"],mobile=request.POST["mobile"],password=request.POST["password"])
        return redirect("Login")
    return render(request,"register.html",{})

def Login(request):
    if request.method=="POST":
        User_register.objects.filter(email=request.POST["email"],password=request.POST["password"])
        return redirect("Home")
    return render(request,"login.html",{})