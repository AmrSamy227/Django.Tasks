from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Login(request):
    return HttpResponse("<h1>welcome to login page</h1>")

def Logout(request):
    return HttpResponse("<h1>welcome to logout page</h1>")

def Register(request):
    return HttpResponse("<h1>welcome to register page</h1>")