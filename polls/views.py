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

    return render(request,'question.html')

def index(request):
    return render(request,'pages/home.html')

