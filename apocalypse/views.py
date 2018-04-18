from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def addevent(request):
    return render(request, 'addevent.html')
