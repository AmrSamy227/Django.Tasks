from django.shortcuts import render
from django.http import HttpResponse

def alltrainees(request):
    trainees = [
        [1, 'Amr', 'Python'],
        [2, 'Sara', 'Java'],
        [3, 'Ali', 'C#']
    ]
    return render(request, 'trainee/list.html', context={'trainees': trainees})


def gettraineeid(request):
    return HttpResponse("<h1>welcome to this trainee</h1>")

def inserttrainee(request):
    return HttpResponse("<h1>welcome to insert trainee</h1>")

def updatetrainee(request, id):
    return HttpResponse(f"<h1>welcome to update trainee {id}</h1>")

def deletetrainee(request, id):
    return HttpResponse(f"<h1>welcome to delete trainee {id}</h1>")

