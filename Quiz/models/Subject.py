'''
Created on Feb 6, 2024

@author: Administrator
'''
from django.db import models

class Subject(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=False,db_column="create_date",editable=True)
    class Meta:
        db_table = 'subject'
        app_label = 'Quiz'
        constraints = [
        models.UniqueConstraint(fields=['code'], name='unique appversion')
    ]