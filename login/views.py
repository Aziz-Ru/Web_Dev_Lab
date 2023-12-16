from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
def index(request):
    if request.path=='/sign_up/':
        return render(request,'pages/sign.html')
     
       
def submitForm(request):
        try:
            if request.method=='GET':
                username=request.GET['username']
                email=request.GET['email']
                password=request.GET['password']
                birthdate=request.GET['birthdate']
                data={
                 'username':username,
                'email':email,
                'password':password,
                'date':birthdate,
                }
            elif request.method=='POST':
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
    
