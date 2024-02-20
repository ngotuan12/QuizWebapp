'''
Created on Feb 6, 2024

@author: Ngô Anh Tuấn
'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required()
def index(request):
    context = {}
    return render(request, "quiz/history.html", context)