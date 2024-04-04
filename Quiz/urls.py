'''
Created on Feb 6, 2024

@author: Ngo Anh Tuan
'''

from django.urls.conf import path
from Quiz.views import Authentication as auth_views
from Quiz.views import Question as question_views
from Quiz.views import Subject as subject_views
from Quiz.views import Exam as exam_views
from Quiz.views import bss as bss_views

from Quiz.views import Practice as practice_views
from Quiz.views import History as history_views
from Quiz.views import Certificate as certificate_views

app_name = 'quiz'

urlpatterns = [
    path('', auth_views.home , name='home'),
    path('question/', question_views.index , name='question'),
    path('question/import/', question_views.question_import , name='question_import'),
    path('question/answer/', question_views.get_question_answer , name='get_question_answer'),
    path('question/delete/<str:question_id>/', question_views.delete , name='question_delete'),
    # subject
    path('subject/', subject_views.index , name='subject'),
    path('subject/add/', subject_views.add , name='subject_add'),
    path('subject/edit/<int:subject_id>/', subject_views.edit , name='subject_edit'),
    path('subject/delete/<str:subject_id>/', subject_views.delete , name='subject_delete'),
    # exam
    path('exam/', exam_views.index , name='exam'),
    path('exam/add', exam_views.add , name='exam_add'),
    path('exam/edit/<int:exam_id>/', exam_views.edit , name='exam_edit'),
    path('exam/delete/<str:exam_id>/', exam_views.delete , name='exam_delete'),
    path('exam/question/random/load/', exam_views.load_random_exam_question , name='load_random_exam_question'),
    # BSS
    path('bss/source', bss_views.source, name='bss_source'),
    path('bss/source/mix', bss_views.source_mix, name='bss_source_mix'),
    path('bss/source/separation', bss_views.source_separation, name='bss_source_separation'),
    # 
    path('practice/', practice_views.index , name='practice'),
    path('history/', history_views.index , name='history'),
    path('certificate/', certificate_views.index , name='certificate'),
    path('sign/out/', auth_views.sign_out , name='sign_out'),
    path('sign/in/', auth_views.sign_in , name='sign_in'),
    path('permission-error/', auth_views.permission_error, name='permission_error'),
    ]
