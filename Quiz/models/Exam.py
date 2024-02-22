from django.db import models
from Quiz.models.Subject import Subject
from Quiz.models.Question import Question


class Exam(models.Model):
    subject = models.ForeignKey(Subject, null=False, on_delete=models.PROTECT, related_name='subject_questions' )
    questions = models.ManyToManyField(
        Question,
        through='ExamQuestion',
    )
    class Meta:
        db_table = 'exam'