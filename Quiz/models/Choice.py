from django.db import models
from Quiz.models import Question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        db_table = 'choice'