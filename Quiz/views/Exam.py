'''
Created on Feb 6, 2024

@author: Ngô Anh Tuấn
'''

import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.views.decorators.http import require_http_methods

from Quiz.models.Exam import Exam
from Quiz.models.Question import Question
from Quiz.models.Subject import Subject
from Quiz.util.DateEncoder import DateTimeEncoder
from Quiz.models.ExamQuestion import ExamQuestion


@login_required()
def index(request):
    context = {}
    exams = Exam.objects.all()
    context.update({'exams':exams})
    return render(request, "quiz/exam/exam-index.html", context)
@login_required()
def add(request):
    context = {}
    subjects = Subject.objects.all()
    context.update({'subjects':subjects})
    try:
        if request.method == 'POST':
            txtListQuestion = request.POST.get('txtListQuestion')
            questions = json.loads(txtListQuestion)
            subject_id = int(request.POST.get('slSubject'))
            # exam
            exam = Exam()
            exam.subject_id = subject_id
            exam.code = request.POST.get('txtCode')
            exam.duration = request.POST.get('txtDuration')
            exam.num_question = request.POST.get('txtNumQuestion')
            exam.create_user = request.user
            exam.save()
            # question
            for index,question in enumerate(questions):
                exam_question = ExamQuestion()
                exam_question.question_id = question.get('id');
                exam_question.exam_id = exam.id
                exam_question.order = index+1
                exam_question.save()
            return redirect(resolve_url('quiz:exam'))
    except Exception as ex:
        context.update({'has_error':str(ex)})
    return render(request, "quiz/exam/exam-add.html", context)
@login_required()
@require_http_methods(["POST", ])
def load_random_exam_question(request):
    try:
        num_question = request.POST['num_question']
        subject_id  = request.POST['subject_id']
        questions = Question.objects.filter(subject_id = subject_id).order_by('?')[:int(num_question)].values()
        return HttpResponse(json.dumps({'handle':'success', 'questions':list(questions)}, cls=DateTimeEncoder) , content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")
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
        # exam questions
        exam_questions = ExamQuestion.objects.filter(exam_id = exam_id)
        exam_questions.delete()
        # exam
        exam = Exam.objects.get(id=int(exam_id))
        exam.delete()
        # check permission error
        return HttpResponse(json.dumps({'handle':'success',}), content_type="application/json");
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")