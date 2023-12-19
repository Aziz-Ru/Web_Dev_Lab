from django.shortcuts import render,redirect
from .models import Question,Answers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["POST"])
def save_question_result(request):
    data = request.data
    question_uid = data.get('question_uid')
    answer_uid  =data.get('answer_uid')
    if question_uid is None and answer_uid is None:
        payload= {'data':'uid Error','status':False}
        return Response(payload)

    question_obj=Question.objects.get(uid =question_uid)
    answer_obj =Answers.objects.get(uid=answer_uid)
    answer_obj.counter+=1
    answer_obj.save()
    payload= {'data':question_obj.calculate_percentage(),'status':True}

    return Response(payload)





def question_detail(request,question_uid):

    try:
        question_obj=Question.objects.get(uid=question_uid)
        context={'question':question_obj}
    
    except Exception as e:
        print(e)
        # return redirect('/')

    return render(request,'question.html',context)

def index(request):
     if request.path=='/':
        data={
            'title':'Home',
            'descrip':'Home Page',
            'list':['PHP','C++','PYTHON','JAVA','JAVASCRIPT','Django','Node JS','HTML','CSS','C','React'],
        }
        template_name='pages/home.html'
     elif request.path=='/about/':
        if request.method=='GET':
            output=request.GET.get('output')
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
    #  elif request.path=='/enroll/':
    #     data={
    #         'title':'Enroll',
    #     }
    #     template_name='check.html'

    
     return render(request,template_name,data)

