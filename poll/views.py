from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def indexes(request):
    if request.path=='/':
        data={
            'title':'Home',
            'descrip':'Home Page',
            'list':['PHP','C++','PYTHON','JAVA','JAVASCRIPT','Django','Node JS','HTML','CSS','C','React'],
        }
        template_name='pages/home.html'
    elif request.path=='/about/':
        data={
            'title':'About',
            'descrip':'About Page'
        }
        template_name='pages/about.html'

    elif request.path=='/services/':
        data={
            'title':'Serivics',
            'descrip':'Services page'
        }
        template_name='pages/services.html'
    elif request.path=='/projects/':
        data={
            'title':'Projects',
            'descrip':'Projects'
        }
        template_name='pages/project.html'
    elif request.path=='/enroll/':
        data={
            'title':'Enroll',
        }
        template_name='check.html'

        

    return render(request,template_name,data)

def signup(request):
        data={}
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
                return HttpResponseRedirect('/about/')

        except:
            pass
        
        template_name='pages/sign.html'
        return render(request,template_name,data)
        



