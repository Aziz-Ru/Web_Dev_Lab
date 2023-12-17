from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import user
def index(request):
    if request.path=='/sign_up/':
        userData=user.objects.all()
        print(userData)
        data={
             'user':userData
        }
        return render(request,'pages/sign.html',data)
     
       
def submitForm(request):
        try:
            if request.method=='POST':
                username=request.POST['username']
                email=request.POST['email']
                password=request.POST['password']
                birthdate=request.POST['birthdate']
                data={
                 'username':username,
                'email':email,
                'password':password,
                'date':birthdate,
                }
        except:
            pass

        return render(request,'pages/submitfrom.html',data)
    
