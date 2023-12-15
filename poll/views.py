from django.shortcuts import render
from django.http import HttpResponse
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
    elif request.path=='/sign_in/':
        data={
            'title':'Sign Form',
            'descrip':'sign',
        }
        template_name='pages/sign.html'

    elif request.path=='/enroll/':
        data={
            'title':'Enroll',
        }
        template_name='check.html'

        

    return render(request,template_name,data)


