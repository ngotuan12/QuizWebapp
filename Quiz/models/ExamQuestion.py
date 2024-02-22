from django.db import models
from Quiz.models.Question import Question
from Quiz.models.Exam import Exam


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, null=False, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, null=False, on_delete=models.PROTECT)
    order = models.IntegerField(default = 0)
    class Meta:
        db_table = 'exam_question'