from django.db import models
from Quiz.models.Subject import Subject
from Quiz.models.Question import Question
from django.contrib.auth.models import User


class Exam(models.Model):
    subject = models.ForeignKey(Subject, null=False, on_delete=models.PROTECT)
    code = models.CharField(max_length=20)
    duration = models.IntegerField()
    num_question = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    questions = models.ManyToManyField(
        Question,
        through='ExamQuestion',
        through_fields=('exam', 'question'),
    )
    class Meta:
        db_table = 'exam'
        constraints = [
        models.UniqueConstraint(fields=['code'], name='unique_exam_code')
    ]
