'''
Created on Feb 6, 2024

@author: Ngô Anh Tuấn
'''

import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from Quiz.models.Exam import Exam


@login_required()
def index(request):
    context = {}
    exams = Exam.objects.all()
    context.update({'exams':exams})
    return render(request, "quiz/exam/exam-index.html", context)
@login_required()
def add(request):
    context = {}
    return render(request, "quiz/exam/exam-add.html", context)
@login_required()
def edit(request,exam_id):
    context = {}
    try:
        exam = Exam.objects.get(id=exam_id)
        context.update({"exam":exam})
        if request.method == 'POST':
            exam.code = request.POST.get('txtCode')
            exam.save()
            return redirect(resolve_url('quiz:exam'))
    except Exception as ex:
        context.update({'has_error':str(ex)})
    return render(request,"quiz/exam/exam-edit.html",context)
@login_required()
def delete(request,exam_id):
    try:
        exam = Exam.objects.get(id=int(exam_id))
        exam.delete()
        # check permission error
        return HttpResponse(json.dumps({'handle':'success',}), content_type="application/json");
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")