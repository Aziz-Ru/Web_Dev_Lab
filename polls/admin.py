from django.contrib import admin
from .models import Question,Answers
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','user']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ['answer_text','question_text','counter']


    def question_text(self,obj):
        return obj.question.question_text


