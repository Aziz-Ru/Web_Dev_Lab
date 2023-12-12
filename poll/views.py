from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def about(request):
    context={
        'title':'About',
    }
    return render(request,'pages/about.html' ,context)

def services(request):
    return render(request,'pages/services.html')

def project(request):
    return render(request,'pages/project.html')
