
from django.db import models
from Quiz.models.Subject import Subject


class Question(models.Model):
    subjects = models.ForeignKey(Subject, null=False, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    class Meta:
        db_table = 'question'
