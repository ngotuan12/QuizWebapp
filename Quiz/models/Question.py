
from django.db import models
from Quiz.models.Subject import Subject


class Question(models.Model):
    subject = models.ForeignKey(Subject, null=False, on_delete=models.PROTECT )
    text = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200,default='',null=True)
    image_url = models.CharField(max_length=200,default='',null=True)
    unit = models.CharField(max_length=30,default='')
    point = models.FloatField(default = 1)
    is_mix = models.BooleanField(default=True)
    class Meta:
        db_table = 'question'
