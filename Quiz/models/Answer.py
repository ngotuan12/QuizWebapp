from django.db import models
from Quiz.models.Question import Question

class Answer(models.Model):
    question = models.ForeignKey(Question,null=False, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_right = models.BooleanField(default=False)
    class Meta:
        db_table = 'answer'