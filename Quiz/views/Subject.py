'''
Created on Feb 6, 2024

@author: Ngô Anh Tuấn
'''

import json

from django.contrib.auth.decorators import login_required
from django.db.models.query import Prefetch
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from Quiz.models import Question
from Quiz.models.Subject import Subject


@login_required()
def index(request):
    context = {'subjects':Subject.objects.prefetch_related(Prefetch("question_set",to_attr="questions"))}
    return render(request, "quiz/subject/subject-index.html", context)
@login_required()
def add(request):
    context = {}
    try:
        if request.method == 'POST':
            subject = Subject()
            subject.code = request.POST.get('txtCode')
            subject.name = request.POST.get('txtName')
            subject.save()
            return redirect(resolve_url('quiz:subject'))
    except Exception as ex:
        context.update({'has_error':str(ex)})
    return render(request, "quiz/subject/subject-add.html", context)
@login_required()
def edit(request,subject_id):
    context = {}
    try:
        subject = Subject.objects.get(id=subject_id)
        context.update({"subject":subject})
        if request.method == 'POST':
            subject.code = request.POST.get('txtCode')
            subject.name = request.POST.get('txtName')
            subject.save()
            return redirect(resolve_url('quiz:subject'))
    except Exception as ex:
        context.update({'has_error':str(ex)})
    return render(request,"quiz/subject/subject-edit.html",context)
@login_required()
def delete(request,subject_id):
    try:
        subject = Subject.objects.get(id=int(subject_id))
        subject.delete()
        # check permission error
        return HttpResponse(json.dumps({'handle':'success',}), content_type="application/json");
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")