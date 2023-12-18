from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid       =models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract =True


class Question(BaseModel):
    user    =models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    question_text=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question_text
    
    def calculate_percentage(self):
        answers=self.answers.all()
        total_count=0
        for ans in answers:
            total_count+=ans.counter
        
        payload=[]
        for ans in answers:
            payload.append(int((ans.counter / total_count)*100))

        return payload
        # formula=C/V*100
    

class Answers(BaseModel):
    question    =models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    answer_text  = models.CharField(max_length=100)
    counter     =models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.answer_text
