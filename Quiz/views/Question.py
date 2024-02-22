'''
Created on Feb 6, 2024

@author: Ngô Anh Tuấn
'''
import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.http import require_http_methods

from Quiz.models.Question import Question
from Quiz.models.Subject import Subject
from Quiz.util.DateEncoder import DateTimeEncoder
from QuizWebapp import settings
from Quiz.models.Answer import Answer


@login_required()
def index(request):
    context = {}
    subject_id = request.GET.get('subject_id')
    subjects = Subject.objects.all()
    # subject
    if subject_id is None:
        subject_id = subjects.first().id
    questions = Question.objects.filter(subject_id = subject_id)
    context.update({'subjects':subjects,'questions':questions})
    context.update({'STATIC_URL':settings.STATIC_URL})
    return render(request, "quiz/question/question-index.html", context)
@login_required()
@require_http_methods(["POST", ])
def get_question_answer(request):
    try:
        question_id  = request.POST['question_id']
        answers = Answer.objects.filter(question_id = question_id)
        return HttpResponse(json.dumps({'handle':'success', 'answers':list(answers)}, cls=DateTimeEncoder) , content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")
@login_required()
@require_http_methods(["POST", ])
def load_subject_question(request):
    try:
        
        subject_id  = request.POST['subject_id']
        questions = Question.objects.filter(subject_id = subject_id)
        return HttpResponse(json.dumps({'handle':'success', 'questions':list(questions)}, cls=DateTimeEncoder) , content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")
@login_required()
def delete(request,question_id):
    try:
        # answer
        answers = Answer.objects.filter(question_id = question_id)
        answers.delete()
        # question
        question = Question.objects.get(id=int(question_id))
        question.delete()
        # check permission error
        return HttpResponse(json.dumps({'handle':'success',}), content_type="application/json");
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")