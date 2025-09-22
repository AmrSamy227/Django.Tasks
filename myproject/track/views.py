from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def alltracks(request):
    tracks=[[1,'python'],[2,'java'],[3,'c#']]
    return render(request,'list.html',context={'tracks':tracks})

def gettrackid(request):
    return HttpResponse("<h1>welcome to this track</h1>")

def inserttrack(request):
    return HttpResponse("<h1>welcome to isert track</h1>")
def updatetrack(request,id):
    return HttpResponse(f"<h1>welcome to update track {id}</h1>")

def deletetrack(request,id):
    return HttpResponse(f"<h1>welcome to delete track {id}</h1>")