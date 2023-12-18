from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name=''),
    path('about/', views.index,name='about'),
    path('services/', views.index,name='services'),
    path('projects/', views.index,name='project'),
    # path('api/save_result/',views.save_question_result),
    # path('polls/<question_uid>/',views.question_detail,name='question_detail'),
]